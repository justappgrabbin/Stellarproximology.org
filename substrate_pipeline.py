"""
Substrate Data Pipeline Adapter
Ports Miessler's TypeScript/Bun data scripts to Python
Connects to real APIs and feeds your Supabase
"""
import os
import json
import csv
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# === API CONFIG ===

API_KEYS = {
    'fred': os.getenv('FRED_API_KEY', ''),  # fred.stlouisfed.org/docs/api
    'census': os.getenv('CENSUS_API_KEY', ''),  # api.census.gov/data/key_signup
    'bls': os.getenv('BLS_API_KEY', ''),  # bls.gov/developers/home
    # CDC WONDER - no key required
    # EPA - email aqs.support@epa.gov
}

# === DATA SOURCE DEFINITIONS (from Substrate) ===

@dataclass
class DataSourceConfig:
    id: str
    name: str
    api_base: str
    endpoints: Dict[str, str]
    update_frequency: str
    rate_limit: str
    dimensions: Dict[str, float]  # library science scores

DATA_SOURCES = {
    'DS-00004': DataSourceConfig(
        id='DS-00004',
        name='FRED Economic Wellbeing',
        api_base='https://api.stlouisfed.org/fred',
        endpoints={
            'debt_service_ratio': '/series/observations?series_id=TDSP',
            'credit_card_delinquency': '/series/observations?series_id=DRCCLACBS',
            'financial_stress': '/series/observations?series_id=STLFSI4',
            'underemployment': '/series/observations?series_id=U6RATE',
            'consumer_sentiment': '/series/observations?series_id=UMCSENT',
            'gini_inequality': '/series/observations?series_id=SIPOVGINIUSA',
        },
        update_frequency='weekly_to_annual',
        rate_limit='120_req/min',
        dimensions={
            'authority': 0.95, 'currency': 0.90, 'objectivity': 0.95,
            'accuracy': 0.95, 'methodology': 0.90, 'coverage': 0.85,
            'reliability': 0.95, 'provenance': 0.95
        }
    ),
    'DS-00005': DataSourceConfig(
        id='DS-00005',
        name='CDC WONDER Mortality',
        api_base='https://wonder.cdc.gov',
        endpoints={
            'drug_overdose': '/controller/datarequest/D176',
            'suicide': '/controller/datarequest/D176',
            'all_cause': '/controller/datarequest/D176',
        },
        update_frequency='annual_1-2yr_lag',
        rate_limit='fair_use',
        dimensions={
            'authority': 0.98, 'currency': 0.60, 'objectivity': 0.95,
            'accuracy': 0.95, 'methodology': 0.90, 'coverage': 0.90,
            'reliability': 0.95, 'provenance': 0.98
        }
    ),
    'DS-00006': DataSourceConfig(
        id='DS-00006',
        name='Census ACS Social',
        api_base='https://api.census.gov/data',
        endpoints={
            'living_alone': '/2022/acs/acs5?get=B25016_001E',
            'commute_time': '/2022/acs/acs5?get=B08303_001E',
            'no_internet': '/2022/acs/acs5?get=B28002_013E',
        },
        update_frequency='annual',
        rate_limit='500_req/day',
        dimensions={
            'authority': 0.95, 'currency': 0.85, 'objectivity': 0.90,
            'accuracy': 0.90, 'methodology': 0.90, 'coverage': 0.95,
            'reliability': 0.90, 'provenance': 0.95
        }
    ),
    'DS-00007': DataSourceConfig(
        id='DS-00007',
        name='BLS JOLTS Labor',
        api_base='https://api.bls.gov/publicAPI/v2/timeseries/data',
        endpoints={
            'quit_rate': '/JTS00000000QUR',
            'job_openings': '/JTS00000000JOL',
            'hire_rate': '/JTS00000000HIR',
            'layoff_rate': '/JTS00000000LAY',
        },
        update_frequency='monthly',
        rate_limit='500_req/day',
        dimensions={
            'authority': 0.95, 'currency': 0.95, 'objectivity': 0.95,
            'accuracy': 0.95, 'methodology': 0.90, 'coverage': 0.90,
            'reliability': 0.95, 'provenance': 0.95
        }
    ),
    'DS-00008': DataSourceConfig(
        id='DS-00008',
        name='EPA Air Quality',
        api_base='https://aqs.epa.gov/data/api',
        endpoints={
            'pm25': '/sampleData?param=88101',
            'ozone': '/sampleData?param=44201',
            'aqi': '/sampleData?param=81102',
        },
        update_frequency='real_time',
        rate_limit='10_req/min',
        dimensions={
            'authority': 0.95, 'currency': 0.98, 'objectivity': 0.95,
            'accuracy': 0.90, 'methodology': 0.90, 'coverage': 0.85,
            'reliability': 0.90, 'provenance': 0.95
        }
    ),
}

# === PIPELINE ENGINE ===

class DataPipeline:
    """
    Fetches data from authoritative sources, structures it as gates
    """

    def __init__(self, source_id: str):
        self.config = DATA_SOURCES.get(source_id)
        if not self.config:
            raise ValueError(f"Unknown source: {source_id}")
        self.source_id = source_id
        self.results = []
        self.errors = []

    def fetch_fred(self, series_id: str, api_key: str) -> Dict:
        """Fetch FRED economic data"""
        url = f"{self.config.api_base}/series/observations"
        params = {
            'series_id': series_id,
            'api_key': api_key,
            'file_type': 'json',
            'observation_start': '2020-01-01',
            'observation_end': datetime.now().strftime('%Y-%m-%d')
        }

        try:
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            observations = data.get('observations', [])
            if not observations:
                return {'status': 'empty', 'count': 0}

            # Convert to structured records
            records = []
            for obs in observations:
                records.append({
                    'date': obs.get('date'),
                    'value': float(obs.get('value', 0)) if obs.get('value') != '.' else None,
                    'series_id': series_id
                })

            return {
                'status': 'success',
                'count': len(records),
                'latest': records[-1] if records else None,
                'records': records[-12:]  # Last 12 observations
            }

        except Exception as e:
            self.errors.append(str(e))
            return {'status': 'error', 'error': str(e)}

    def fetch_bls(self, series_id: str, api_key: str) -> Dict:
        """Fetch BLS labor data"""
        url = self.config.api_base
        headers = {'Content-Type': 'application/json'}
        payload = {
            'seriesid': [series_id],
            'startyear': '2023',
            'endyear': datetime.now().strftime('%Y'),
            'registrationkey': api_key
        }

        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            series = data.get('Results', {}).get('series', [])
            if not series:
                return {'status': 'empty'}

            records = []
            for item in series[0].get('data', []):
                records.append({
                    'year': item.get('year'),
                    'period': item.get('period'),
                    'value': float(item.get('value', 0)),
                    'series_id': series_id
                })

            return {
                'status': 'success',
                'count': len(records),
                'latest': records[-1] if records else None,
                'records': records[-12:]
            }

        except Exception as e:
            self.errors.append(str(e))
            return {'status': 'error', 'error': str(e)}

    def run(self, api_keys: Dict[str, str] = None) -> Dict:
        """Execute full pipeline for this data source"""
        keys = api_keys or API_KEYS

        print(f"\n[PIPELINE] Running {self.config.name} ({self.source_id})")
        print(f"  Endpoints: {len(self.config.endpoints)}")

        all_results = {}

        for endpoint_name, endpoint_path in self.config.endpoints.items():
            print(f"  Fetching {endpoint_name}...")

            if self.source_id == 'DS-00004':  # FRED
                result = self.fetch_fred(endpoint_path.split('=')[-1], keys.get('fred', ''))
            elif self.source_id == 'DS-00007':  # BLS
                result = self.fetch_bls(endpoint_path, keys.get('bls', ''))
            else:
                result = {'status': 'not_implemented', 'source': self.source_id}

            all_results[endpoint_name] = result

            # Rate limit respect
            time.sleep(1)

        # Build gate from results
        gate = self._build_data_gate(all_results)

        return {
            'source': self.source_id,
            'name': self.config.name,
            'run_at': datetime.now().isoformat(),
            'results': all_results,
            'gate': gate,
            'errors': self.errors,
            'dimensions': self.config.dimensions
        }

    def _build_data_gate(self, results: Dict) -> Dict:
        """Convert pipeline results to a Substrate-style Data gate"""
        # Calculate composite scores from actual data
        latest_values = {}
        for endpoint, result in results.items():
            if result.get('status') == 'success' and result.get('latest'):
                latest_values[endpoint] = result['latest']

        return {
            'id': self.source_id,
            'type': 'DataSource',
            'title': self.config.name,
            'description': f"Wellbeing data from {self.config.name}. Updated {self.config.update_frequency}.",
            'api_endpoint': self.config.api_base,
            'update_frequency': self.config.update_frequency,
            'latest_values': latest_values,
            'library_scores': self.config.dimensions,
            'composite_score': sum(self.config.dimensions.values()) / len(self.config.dimensions),
            'run_at': datetime.now().isoformat()
        }


# === ORCHESTRATOR ===

class PipelineOrchestrator:
    """
    Runs all data pipelines and outputs structured gates
    """

    def __init__(self, api_keys: Dict[str, str] = None):
        self.api_keys = api_keys or API_KEYS
        self.pipelines = []
        self.all_gates = []

    def run_all(self, source_ids: List[str] = None):
        """Run specified pipelines or all"""
        ids = source_ids or list(DATA_SOURCES.keys())

        print("="*60)
        print("SUBSTRATE DATA PIPELINE ORCHESTRATOR")
        print("="*60)

        for sid in ids:
            try:
                pipeline = DataPipeline(sid)
                result = pipeline.run(self.api_keys)
                self.pipelines.append(result)

                if result.get('gate'):
                    self.all_gates.append(result['gate'])

            except Exception as e:
                print(f"  ERROR: {e}")

        return self

    def export_gates(self, path: str = 'data_gates.json'):
        """Export all data gates as JSON"""
        export = {
            'meta': {
                'generated_at': datetime.now().isoformat(),
                'total_sources': len(self.pipelines),
                'total_gates': len(self.all_gates),
            },
            'gates': self.all_gates,
            'pipeline_results': [
                {
                    'source': p['source'],
                    'name': p['name'],
                    'errors': p['errors'],
                    'run_at': p['run_at']
                }
                for p in self.pipelines
            ]
        }

        with open(path, 'w') as f:
            json.dump(export, f, indent=2, default=str)

        print(f"\n[EXPORT] Saved {len(self.all_gates)} gates to {path}")
        return export

    def generate_supabase_sql(self) -> str:
        """Generate SQL to insert gates into Supabase"""
        sql = []
        sql.append("-- Auto-generated from Substrate Pipeline Orchestrator")
        sql.append(f"-- Generated: {datetime.now().isoformat()}")
        sql.append("")

        for gate in self.all_gates:
            dims = gate.get('library_scores', {})
            latest = json.dumps(gate.get('latest_values', {}))

            sql.append(f"""
INSERT INTO substrate_gates (
    id, type, title, description, api_endpoint, update_frequency,
    authority_score, currency_score, objectivity_score, accuracy_score,
    methodology_score, coverage_score, reliability_score, provenance_score,
    metadata
) VALUES (
    '{gate['id']}', 'DataSource', '{gate['title']}', '{gate['description'][:200]}',
    '{gate['api_endpoint']}', '{gate['update_frequency']}',
    {dims.get('authority', 0)}, {dims.get('currency', 0)}, 
    {dims.get('objectivity', 0)}, {dims.get('accuracy', 0)},
    {dims.get('methodology', 0)}, {dims.get('coverage', 0)},
    {dims.get('reliability', 0)}, {dims.get('provenance', 0)},
    '{{"latest_values": {latest}, "composite": {gate.get('composite_score', 0)}}}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    metadata = EXCLUDED.metadata;
""")

        return "\n".join(sql)


# === CLI ===
if __name__ == '__main__':
    import sys

    # Check for API keys
    if not API_KEYS.get('fred'):
        print("WARNING: No FRED_API_KEY set. Get one at fred.stlouisfed.org/docs/api")
        print("Set it: export FRED_API_KEY='your_key'")

    # Run orchestrator
    orch = PipelineOrchestrator()

    # Run just FRED first (most accessible)
    orch.run_all(['DS-00004'])

    # Export
    orch.export_gates('data_gates.json')

    # Generate SQL
    sql = orch.generate_supabase_sql()
    with open('data_gates.sql', 'w') as f:
        f.write(sql)
    print("Saved data_gates.sql")
