"""
Substrate Engine API Server
FastAPI backend for your 5D chat orchestrator
Runs on Render (synthia-server.onrender)
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import json
import os
from datetime import datetime

# Import our modules
from substrate_ingestor import SubstrateIngestor, Gate, Problem, Solution, Argument, DataSource, EmergentLink
from substrate_pipeline import DataPipeline, PipelineOrchestrator, DATA_SOURCES

app = FastAPI(
    title="Substrate Engine",
    description="5D Semantic Topology API - Ingests, queries, and evolves knowledge",
    version="0.1.0"
)

# CORS for your PWA
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lock this down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === STATE ===
# In production, this lives in Supabase. For now, in-memory with file persistence.

class EngineState:
    def __init__(self):
        self.gates: Dict[str, Gate] = {}
        self.links: List[EmergentLink] = []
        self.data_cache: Dict[str, Any] = {}
        self.ingestor: Optional[SubstrateIngestor] = None

    def load_from_substrate(self, repo_path: str = './Substrate'):
        """Load gates from cloned Substrate repo"""
        if os.path.exists(repo_path):
            self.ingestor = SubstrateIngestor(repo_path)
            self.ingestor.scan_structure()
            self.ingestor.build_knowledge_graph()
            self.gates.update(self.ingestor.gates)
            self.links.extend(self.ingestor.links)
            return len(self.gates)
        return 0

    def load_data_gates(self, path: str = 'data_gates.json'):
        """Load live data gates from pipeline output"""
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            for gate_data in data.get('gates', []):
                gate = DataSource(
                    id=gate_data['id'],
                    type='DataSource',
                    title=gate_data['title'],
                    description=gate_data.get('description', ''),
                    api_endpoint=gate_data.get('api_endpoint', ''),
                    update_frequency=gate_data.get('update_frequency', ''),
                    metadata=gate_data.get('latest_values', {})
                )
                self.gates[gate.id] = gate
            return len(data.get('gates', []))
        return 0

    def query_gates(self, gate_type: Optional[str] = None, 
                   search: Optional[str] = None,
                   limit: int = 50) -> List[Dict]:
        """Query gates with filters"""
        results = []
        for gate in self.gates.values():
            if gate_type and gate.type != gate_type:
                continue
            if search and search.lower() not in gate.title.lower():
                continue
            results.append(gate.to_dict())
        return results[:limit]

    def get_gate_network(self, gate_id: str, depth: int = 1) -> Dict:
        """Get a gate and its connected network"""
        if gate_id not in self.gates:
            return {'error': 'Gate not found'}

        gate = self.gates[gate_id]
        network = {
            'center': gate.to_dict(),
            'connected': [],
            'links': []
        }

        # Find direct links
        for link in self.links:
            if link.from_gate == gate_id or link.to_gate == gate_id:
                network['links'].append(link.to_dict())
                other_id = link.to_gate if link.from_gate == gate_id else link.from_gate
                if other_id in self.gates:
                    network['connected'].append(self.gates[other_id].to_dict())

        return network

state = EngineState()

# === API MODELS ===

class QueryRequest(BaseModel):
    question: str
    gate_types: Optional[List[str]] = None
    include_data: bool = True
    max_results: int = 10

class GateResponse(BaseModel):
    id: str
    type: str
    title: str
    description: str
    links: List[str]
    metadata: Dict[str, Any]

class NetworkResponse(BaseModel):
    center: Dict[str, Any]
    connected: List[Dict[str, Any]]
    links: List[Dict[str, Any]]

class IngestRequest(BaseModel):
    repo_path: str = "./Substrate"
    source_type: str = "substrate"  # or "custom"

class DataRefreshRequest(BaseModel):
    source_ids: Optional[List[str]] = None  # None = all
    api_keys: Optional[Dict[str, str]] = None

# === ENDPOINTS ===

@app.get("/")
def root():
    return {
        "engine": "Substrate 5D",
        "status": "running",
        "gates_loaded": len(state.gates),
        "links_loaded": len(state.links),
        "version": "0.1.0"
    }

@app.get("/gates")
def list_gates(
    type: Optional[str] = Query(None, description="Filter by gate type"),
    search: Optional[str] = Query(None, description="Search in title"),
    limit: int = Query(50, ge=1, le=200)
):
    """List all gates, optionally filtered"""
    return state.query_gates(gate_type=type, search=search, limit=limit)

@app.get("/gates/{gate_id}")
def get_gate(gate_id: str):
    """Get a specific gate by ID"""
    if gate_id not in state.gates:
        raise HTTPException(status_code=404, detail="Gate not found")
    return state.gates[gate_id].to_dict()

@app.get("/gates/{gate_id}/network")
def get_network(gate_id: str, depth: int = Query(1, ge=1, le=3)):
    """Get gate and its connected network"""
    return state.get_gate_network(gate_id, depth)

@app.post("/query")
def query_knowledge(request: QueryRequest):
    """
    Main query endpoint for your chat PWA.
    Takes a natural language question, returns relevant gates + data.
    """
    # Simple keyword matching (replace with LLM/embedding in v2)
    keywords = request.question.lower().split()

    scored_gates = []
    for gate in state.gates.values():
        score = 0
        text = f"{gate.title} {gate.description}".lower()
        for kw in keywords:
            if kw in text:
                score += 1
        if score > 0:
            scored_gates.append((score, gate.to_dict()))

    scored_gates.sort(reverse=True, key=lambda x: x[0])
    top_gates = [g[1] for g in scored_gates[:request.max_results]]

    # Include live data if requested
    data_context = {}
    if request.include_data:
        for gate in state.gates.values():
            if gate.type == 'DataSource' and gate.id.startswith('DS-'):
                data_context[gate.id] = {
                    'title': gate.title,
                    'latest': gate.metadata
                }

    return {
        "query": request.question,
        "gates": top_gates,
        "data_context": data_context,
        "suggested_links": [],  # AI would generate these
        "timestamp": datetime.now().isoformat()
    }

@app.post("/ingest")
def ingest_repo(request: IngestRequest):
    """Ingest a Substrate repo or custom directory"""
    count = state.load_from_substrate(request.repo_path)
    return {
        "ingested": count,
        "total_gates": len(state.gates),
        "repo_path": request.repo_path
    }

@app.post("/data/refresh")
def refresh_data(request: DataRefreshRequest):
    """Run data pipelines and refresh live data gates"""
    orch = PipelineOrchestrator(api_keys=request.api_keys)

    # Run requested sources
    ids = request.source_ids or list(DATA_SOURCES.keys())
    orch.run_all(ids)
    orch.export_gates('data_gates.json')

    # Reload into state
    loaded = state.load_data_gates('data_gates.json')

    return {
        "sources_run": len(ids),
        "gates_updated": loaded,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/dimensions")
def get_dimensions():
    """Get the 5D structure and gate type mappings"""
    return {
        "dimensions": {
            "1": {"name": "Being/Perspective", "gate_types": ["Problem"]},
            "2": {"name": "Movement/Evolution", "gate_types": ["Solution", "Plan"]},
            "3": {"name": "Design/Reasoning", "gate_types": ["Argument", "Claim"]},
            "4": {"name": "Space/Field", "gate_types": ["DataSource", "Project"]},
            "5": {"name": "Emergence", "gate_types": ["EmergentLink", "Idea"]}
        },
        "gate_counts": {
            t: len([g for g in state.gates.values() if g.type == t])
            for t in set(g.type for g in state.gates.values())
        }
    }

@app.get("/health")
def health():
    return {"status": "ok", "gates": len(state.gates), "links": len(state.links)}

# === STARTUP ===

@app.on_event("startup")
def startup():
    """Auto-load on server start"""
    print("[STARTUP] Substrate Engine initializing...")

    # Try to load from Substrate repo if it exists
    if os.path.exists('./Substrate'):
        count = state.load_from_substrate('./Substrate')
        print(f"  Loaded {count} gates from Substrate repo")

    # Try to load data gates if they exist
    if os.path.exists('data_gates.json'):
        count = state.load_data_gates('data_gates.json')
        print(f"  Loaded {count} data gates")

    print(f"[READY] {len(state.gates)} gates, {len(state.links)} links")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
