"""
Substrate Ingestor - Adapts Miessler's Substrate to your 5D Engine
Parses repo structure, extracts schemas, ingests data sources
"""
import os
import re
import json
import csv
import glob
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime

# === DIMENSIONAL GATE SCHEMAS (from Substrate) ===

@dataclass
class Gate:
    """Base gate - all dimensional objects inherit this"""
    id: str
    type: str  # Problem, Solution, Argument, Data, etc.
    title: str
    description: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    source_repo: str = "substrate"
    links: List[str] = field(default_factory=list)  # IDs of connected gates
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return asdict(self)

@dataclass  
class Problem(Gate):
    """1st Dimension - Being/Perspective"""
    evidence: str = ""
    severity: str = "medium"  # low, medium, high, critical
    affected_population: str = ""

@dataclass
class Solution(Gate):
    """2nd Dimension - Movement/Evolution"""
    approach: str = ""
    results: str = ""
    implementation_status: str = "proposed"  # proposed, active, completed, failed

@dataclass
class Argument(Gate):
    """3rd Dimension - Design/Reasoning"""
    reasoning: str = ""
    quality_score: float = 0.0
    supporting_claims: List[str] = field(default_factory=list)

@dataclass
class DataSource(Gate):
    """4th Dimension - Space/Field"""
    api_endpoint: str = ""
    update_frequency: str = ""
    authority_score: float = 0.0  # 0-1
    currency_score: float = 0.0
    objectivity_score: float = 0.0
    accuracy_score: float = 0.0
    methodology_score: float = 0.0
    coverage_score: float = 0.0
    reliability_score: float = 0.0
    provenance_score: float = 0.0
    last_updated: str = ""

@dataclass
class EmergentLink(Gate):
    """5th Dimension - Emergence/AI Discovered"""
    from_gate: str = ""
    to_gate: str = ""
    link_type: str = "suggests"  # suggests, contradicts, supports, enables
    confidence: float = 0.0
    discovered_by: str = "ai"
    validated: bool = False

# === INGESTOR ENGINE ===

class SubstrateIngestor:
    """
    Reads a Substrate repo and converts it to dimensional gates
    """

    GATE_TYPES = {
        'Problems': Problem,
        'Solutions': Solution,
        'Arguments': Argument,
        'Data': DataSource,
        'Data-Sources': DataSource,
        'Claims': Gate,
        'Plans': Gate,
        'Ideas': Gate,
        'People': Gate,
        'Organizations': Gate,
        'Projects': Gate,
        'Values': Gate,
    }

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.gates: Dict[str, Gate] = {}
        self.links: List[EmergentLink] = []
        self.data_pipelines: Dict[str, Dict] = {}

    def scan_structure(self):
        """Scan repo and catalog all gates"""
        print(f"\n[SCAN] Reading {self.repo_path}...")

        for gate_dir, gate_class in self.GATE_TYPES.items():
            dir_path = self.repo_path / gate_dir
            if not dir_path.exists():
                continue

            print(f"  Found {gate_dir}/")

            # Find all markdown files (each is a gate)
            md_files = list(dir_path.rglob("*.md"))
            csv_files = list(dir_path.rglob("*.csv"))

            for md_file in md_files[:5]:  # Sample first 5
                gate = self._parse_markdown_gate(md_file, gate_class)
                if gate:
                    self.gates[gate.id] = gate

            # Parse CSV data files
            for csv_file in csv_files[:3]:
                self._parse_csv_data(csv_file, gate_dir)

        print(f"  Total gates ingested: {len(self.gates)}")
        return self

    def _parse_markdown_gate(self, file_path: Path, gate_class) -> Optional[Gate]:
        """Parse a markdown file into a gate object"""
        try:
            content = file_path.read_text()

            # Extract ID from filename or frontmatter
            gate_id = self._extract_id(file_path, content)

            # Extract title (first H1)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem

            # Extract description (first paragraph after title)
            desc_match = re.search(r'^#\s+.+\n\n(.+?)(?=\n##|\n\n##|$)', 
                                   content, re.MULTILINE | re.DOTALL)
            description = desc_match.group(1).strip() if desc_match else ""

            # Extract links (IDs referenced in content)
            links = re.findall(r'[A-Z]-\d{5}', content)

            # Build gate
            gate = gate_class(
                id=gate_id,
                type=gate_class.__name__,
                title=title,
                description=description,
                links=links,
                metadata={
                    'file_path': str(file_path),
                    'word_count': len(content.split()),
                }
            )

            return gate

        except Exception as e:
            print(f"    Error parsing {file_path}: {e}")
            return None

    def _extract_id(self, file_path: Path, content: str) -> str:
        """Extract gate ID from filename or content"""
        # Try filename pattern: P-00001, S-00001, etc.
        match = re.search(r'([A-Z])-(\d{5})', file_path.name)
        if match:
            return f"{match.group(1)}-{match.group(2)}"

        # Try frontmatter
        fm_match = re.search(r'^id:\s*(.+)$', content, re.MULTILINE)
        if fm_match:
            return fm_match.group(1).strip()

        # Fallback: use relative path
        return file_path.stem.replace(' ', '-')

    def _parse_csv_data(self, file_path: Path, gate_type: str):
        """Parse CSV data files into structured records"""
        try:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                records = list(reader)

            self.data_pipelines[file_path.stem] = {
                'type': gate_type,
                'path': str(file_path),
                'records': len(records),
                'columns': list(records[0].keys()) if records else [],
                'sample': records[:2] if records else []
            }
            print(f"    CSV: {file_path.name} ({len(records)} records)")

        except Exception as e:
            print(f"    Error parsing CSV {file_path}: {e}")

    def extract_data_scripts(self):
        """Find and catalog TypeScript/Bun data update scripts"""
        scripts_dir = self.repo_path / 'scripts'
        data_sources_dir = self.repo_path / 'Data-Sources'

        update_scripts = []

        for search_dir in [scripts_dir, data_sources_dir]:
            if search_dir.exists():
                for ts_file in search_dir.rglob("*.ts"):
                    if 'update' in ts_file.name.lower():
                        update_scripts.append({
                            'path': str(ts_file),
                            'name': ts_file.name,
                            'size': ts_file.stat().st_size
                        })

        print(f"\n[SCRIPTS] Found {len(update_scripts)} update scripts")
        for s in update_scripts[:5]:
            print(f"  {s['name']} ({s['size']} bytes)")

        self.data_pipelines['update_scripts'] = update_scripts
        return update_scripts

    def build_knowledge_graph(self):
        """Build graph from extracted links between gates"""
        print(f"\n[GRAPH] Building relationships...")

        for gate_id, gate in self.gates.items():
            for linked_id in gate.links:
                if linked_id in self.gates:
                    link = EmergentLink(
                        id=f"LINK-{gate_id}-{linked_id}",
                        type="EmergentLink",
                        title=f"{gate.type} → {self.gates[linked_id].type}",
                        from_gate=gate_id,
                        to_gate=linked_id,
                        link_type="connects_to",
                        confidence=0.8,
                        discovered_by="substrate_parser"
                    )
                    self.links.append(link)

        print(f"  Total links: {len(self.links)}")
        return self.links

    def export_to_json(self, output_path: str):
        """Export all gates and links to JSON"""
        export = {
            'meta': {
                'source': 'danielmiessler/Substrate',
                'ingested_at': datetime.now().isoformat(),
                'total_gates': len(self.gates),
                'total_links': len(self.links),
                'gate_types': list(set(g.type for g in self.gates.values())),
            },
            'gates': {k: v.to_dict() for k, v in self.gates.items()},
            'links': [l.to_dict() for l in self.links],
            'data_pipelines': self.data_pipelines
        }

        with open(output_path, 'w') as f:
            json.dump(export, f, indent=2, default=str)

        print(f"\n[EXPORT] Saved to {output_path}")
        return export


# === SUPABASE BRIDGE ===

class SupabaseBridge:
    """
    Connects ingested gates to your Supabase instance
    """

    def __init__(self, url: str, key: str):
        self.url = url.rstrip('/')
        self.key = key
        self.headers = {
            'apikey': key,
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }

    def sync_gates(self, gates: Dict[str, Gate]):
        """Push gates to Supabase table"""
        # This would use supabase-py client
        # For now, generate SQL schema

        schema_sql = """
-- Substrate Gates Table (for your Supabase)
CREATE TABLE IF NOT EXISTS substrate_gates (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    source_repo TEXT DEFAULT 'substrate',
    links TEXT[], -- array of linked gate IDs
    metadata JSONB,
    -- Dimensional scores (library science)
    authority_score FLOAT,
    currency_score FLOAT,
    objectivity_score FLOAT,
    accuracy_score FLOAT,
    methodology_score FLOAT,
    coverage_score FLOAT,
    reliability_score FLOAT,
    provenance_score FLOAT
);

-- Emergent Links Table (5th dimension)
CREATE TABLE IF NOT EXISTS substrate_links (
    id TEXT PRIMARY KEY,
    from_gate TEXT REFERENCES substrate_gates(id),
    to_gate TEXT REFERENCES substrate_gates(id),
    link_type TEXT,
    confidence FLOAT,
    discovered_by TEXT,
    validated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Data Pipeline Tracking
CREATE TABLE IF NOT EXISTS data_pipelines (
    id SERIAL PRIMARY KEY,
    name TEXT,
    source_type TEXT,
    api_endpoint TEXT,
    last_run TIMESTAMP,
    records_ingested INT,
    status TEXT,
    config JSONB
);
"""
        return schema_sql

    def generate_insert_statements(self, gates: Dict[str, Gate]) -> List[str]:
        """Generate SQL INSERTs for gates"""
        inserts = []
        for gate in gates.values():
            d = gate.to_dict()
            # Escape single quotes
            title = d['title'].replace("'", "''")
            desc = d['description'].replace("'", "''")

            sql = f"""
INSERT INTO substrate_gates (id, type, title, description, links, metadata)
VALUES ('{d['id']}', '{d['type']}', '{title}', '{desc}', 
        ARRAY{d['links']}, '{json.dumps(d['metadata'])}'::jsonb)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    links = EXCLUDED.links,
    metadata = EXCLUDED.metadata;
"""
            inserts.append(sql)
        return inserts


# === MAIN ===
if __name__ == '__main__':
    import sys

    repo_path = sys.argv[1] if len(sys.argv) > 1 else './Substrate'

    # Run ingestor
    ingestor = SubstrateIngestor(repo_path)
    ingestor.scan_structure()
    ingestor.extract_data_scripts()
    ingestor.build_knowledge_graph()
    ingestor.export_to_json('substrate_ingested.json')

    # Generate Supabase schema
    bridge = SupabaseBridge(
        url='https://leisphnjslcuepflefri.supabase.co',
        key='sb_publishable_r875ycY951IHyew2SwXEmg_qMOgv9AW'
    )

    schema = bridge.sync_gates(ingestor.gates)
    with open('supabase_schema.sql', 'w') as f:
        f.write(schema)

    inserts = bridge.generate_insert_statements(ingestor.gates)
    with open('supabase_inserts.sql', 'w') as f:
        f.write('\n'.join(inserts[:50]))  # First 50

    print("\n[DONE] Files generated:")
    print("  - substrate_ingested.json")
    print("  - supabase_schema.sql")
    print("  - supabase_inserts.sql")
