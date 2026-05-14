
# lab_logic.py - YOU-N-I-VERSE Lab Experiment Engine

from flask import request
import uuid
from datetime import datetime, timedelta
import json
import os

class FieldTestingFramework:
    def __init__(self):
        self.experiments = {}
        self.data_points = {}
        
    def create_experiment(self, name: str, hypothesis: str, test_type: str, duration_days: int = 7):
        exp_id = str(uuid.uuid4())
        self.experiments[exp_id] = {
            "id": exp_id,
            "name": name,
            "hypothesis": hypothesis,
            "test_type": test_type,
            "duration_days": duration_days,
            "start_date": datetime.now(),
            "end_date": datetime.now() + timedelta(days=duration_days),
            "status": "active"
        }
        self.data_points[exp_id] = []
        return exp_id
    
    def add_data_point(self, experiment_id: str, user_id: str, measurement_data):
        if experiment_id not in self.data_points:
            return False
        
        data_point = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "data": measurement_data,
            "id": str(uuid.uuid4())
        }
        
        self.data_points[experiment_id].append(data_point)
        return True
    
    def analyze_experiment(self, experiment_id: str):
        if experiment_id not in self.experiments:
            return {"error": "Experiment not found"}
        
        experiment = self.experiments[experiment_id]
        data_points = self.data_points.get(experiment_id, [])
        
        # Basic analysis
        total_points = len(data_points)
        if total_points == 0:
            return {"experiment": experiment, "analysis": "No data points collected yet"}
        
        # Calculate averages and patterns
        coherence_values = []
        gate_values = []
        
        for point in data_points:
            data = point.get("data", {})
            if "coherence" in data:
                coherence_values.append(data["coherence"])
            if "gates" in data:
                gate_values.append(data["gates"])
        
        analysis = {
            "total_data_points": total_points,
            "avg_coherence": sum(coherence_values) / len(coherence_values) if coherence_values else 0,
            "avg_gate_activations": sum(gate_values) / len(gate_values) if gate_values else 0,
            "trend": "increasing" if len(coherence_values) > 1 and coherence_values[-1] > coherence_values[0] else "stable"
        }
        
        return {"experiment": experiment, "analysis": analysis, "data_points": data_points}

class LabExperimentEngine:
    def __init__(self):
        self.framework = FieldTestingFramework()
        self.active_sessions = {}  # session_id -> experiment_id

    def start_experiment(self, user_id: str, name: str, hypothesis: str, test_type: str, duration_days: int = 7):
        exp_id = self.framework.create_experiment(name, hypothesis, test_type, duration_days)
        session_id = str(uuid.uuid4())
        self.active_sessions[session_id] = {
            "experiment_id": exp_id,
            "user_id": user_id
        }
        return {"session_id": session_id, "experiment_id": exp_id}

    def submit_data_point(self, session_id: str, measurement_data):
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Invalid session"}

        success = self.framework.add_data_point(
            session["experiment_id"],
            session["user_id"],
            measurement_data
        )
        return {"success": success}

    def analyze(self, experiment_id: str):
        return self.framework.analyze_experiment(experiment_id)
    
    def get_active_experiments(self, user_id: str):
        user_experiments = []
        for session_id, session in self.active_sessions.items():
            if session["user_id"] == user_id:
                exp_id = session["experiment_id"]
                if exp_id in self.framework.experiments:
                    experiment = self.framework.experiments[exp_id]
                    user_experiments.append({
                        "session_id": session_id,
                        "experiment": experiment
                    })
        return user_experiments

# Instance for app.py import
lab_engine = LabExperimentEngine()
