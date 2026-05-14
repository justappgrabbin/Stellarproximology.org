
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Callable, Any
import json
import uuid

class IncubationTrigger:
    def __init__(self, trigger_type: str, threshold: float, description: str, completed: bool = False):
        self.type = trigger_type
        self.threshold = threshold
        self.description = description
        self.completed = completed

class IncubationReward:
    def __init__(self, reward_type: str, value: float, description: str):
        self.type = reward_type
        self.value = value
        self.description = description

class IncubationStage:
    def __init__(self, stage_id: str, name: str, description: str, required_coherence: float,
                 required_gate_activations: int, required_memory_imprints: int, duration: float,
                 triggers: List[IncubationTrigger], rewards: List[IncubationReward]):
        self.id = stage_id
        self.name = name
        self.description = description
        self.required_coherence = required_coherence
        self.required_gate_activations = required_gate_activations
        self.required_memory_imprints = required_memory_imprints
        self.duration = duration  # in hours
        self.triggers = triggers
        self.rewards = rewards

class ActiveIncubation:
    def __init__(self, incubation_id: str, stage_id: str, start_time: datetime,
                 current_triggers: List[IncubationTrigger], estimated_completion: datetime):
        self.id = incubation_id
        self.stage_id = stage_id
        self.start_time = start_time
        self.progress_percent = 0.0
        self.current_triggers = current_triggers
        self.estimated_completion = estimated_completion
        self.is_ready = False

class ResonanceSnapshot:
    def __init__(self, timestamp: datetime, coherence_level: float, active_gates: int,
                 field_stability: float, waveform_pattern: str, memory_resonance: float):
        self.timestamp = timestamp
        self.coherence_level = coherence_level
        self.active_gates = active_gates
        self.field_stability = field_stability
        self.waveform_pattern = waveform_pattern
        self.memory_resonance = memory_resonance

class FieldIncubationState:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.current_stage = 'field_awakening'
        self.field_maturity = 0.0
        self.total_incubation_time = 0.0
        self.stage_progress = {}
        self.completed_stages = []
        self.active_incubations = []
        self.resonance_history = []

# Predefined incubation stages
INCUBATION_STAGES = [
    IncubationStage(
        stage_id='field_awakening',
        name='Field Awakening',
        description='Initial recognition of your energetic field patterns',
        required_coherence=25,
        required_gate_activations=3,
        required_memory_imprints=0,
        duration=2,  # 2 hours
        triggers=[
            IncubationTrigger('coherence', 25, 'Maintain 25% coherence for 30 minutes'),
            IncubationTrigger('gate_activation', 3, 'Activate at least 3 unique gates'),
            IncubationTrigger('time_spent', 120, 'Spend 2 hours exploring your field')  # 120 minutes
        ],
        rewards=[
            IncubationReward('field_expansion', 10, 'Field sensitivity increased by 10%'),
            IncubationReward('new_trait_unlock', 1, 'Unlock basic trait resonance viewing')
        ]
    ),
    IncubationStage(
        stage_id='resonance_tuning',
        name='Resonance Tuning',
        description='Learning to fine-tune your field resonance patterns',
        required_coherence=45,
        required_gate_activations=7,
        required_memory_imprints=5,
        duration=6,
        triggers=[
            IncubationTrigger('coherence', 45, 'Achieve 45% coherence stability'),
            IncubationTrigger('waveform_stability', 60, 'Maintain stable waveform for 60 minutes'),
            IncubationTrigger('memory_resonance', 5, 'Create 5 resonant memory imprints')
        ],
        rewards=[
            IncubationReward('resonance_boost', 15, 'Base resonance increased by 15%'),
            IncubationReward('glyph_access', 3, 'Access to 3 advanced glyph combinations')
        ]
    ),
    IncubationStage(
        stage_id='field_mastery',
        name='Field Mastery',
        description='Advanced field manipulation and coherence control',
        required_coherence=70,
        required_gate_activations=15,
        required_memory_imprints=12,
        duration=12,
        triggers=[
            IncubationTrigger('coherence', 70, 'Sustain 70% coherence for extended periods'),
            IncubationTrigger('gate_activation', 15, 'Master activation of 15+ unique gates'),
            IncubationTrigger('glyph_combination', 10, 'Create 10 successful glyph resonance patterns')
        ],
        rewards=[
            IncubationReward('field_expansion', 25, 'Major field capacity expansion'),
            IncubationReward('memory_capacity', 50, 'Memory bank capacity doubled')
        ]
    ),
    IncubationStage(
        stage_id='consciousness_integration',
        name='Consciousness Integration',
        description='Full integration of field awareness with daily consciousness',
        required_coherence=85,
        required_gate_activations=25,
        required_memory_imprints=20,
        duration=24,
        triggers=[
            IncubationTrigger('coherence', 85, 'Achieve 85%+ coherence consistently'),
            IncubationTrigger('memory_resonance', 20, 'Maintain 20+ active memory resonances'),
            IncubationTrigger('waveform_stability', 95, 'Near-perfect waveform stability')
        ],
        rewards=[
            IncubationReward('new_trait_unlock', 5, 'Unlock all advanced trait combinations'),
            IncubationReward('field_expansion', 50, 'Master-level field expansion')
        ]
    )
]

class FieldIncubationEngine:
    def __init__(self, user_id: str, initial_state: Optional[Dict] = None):
        self.state = FieldIncubationState(user_id)
        self.progress_callbacks = []
        
        if initial_state:
            for key, value in initial_state.items():
                if hasattr(self.state, key):
                    setattr(self.state, key, value)

    def start_incubation(self, stage_id: str) -> Optional[ActiveIncubation]:
        """Start a new incubation process"""
        stage = next((s for s in INCUBATION_STAGES if s.id == stage_id), None)
        if not stage:
            return None

        # Check prerequisites
        if not self.can_start_stage(stage):
            raise ValueError(f"Prerequisites not met for stage: {stage.name}")

        incubation = ActiveIncubation(
            incubation_id=f"{stage_id}_{int(datetime.now().timestamp())}",
            stage_id=stage_id,
            start_time=datetime.now(),
            current_triggers=[
                IncubationTrigger(t.type, t.threshold, t.description, t.completed)
                for t in stage.triggers
            ],
            estimated_completion=datetime.now() + timedelta(hours=stage.duration)
        )

        self.state.active_incubations.append(incubation)
        return incubation

    def update_field_metrics(self, metrics: Dict[str, Any]):
        """Update field metrics and check for trigger completions"""
        # Create resonance snapshot
        snapshot = ResonanceSnapshot(
            timestamp=datetime.now(),
            coherence_level=metrics.get('coherence', 0),
            active_gates=metrics.get('active_gates', 0),
            field_stability=metrics.get('waveform_stability', 0),
            waveform_pattern=self.generate_waveform_pattern(metrics),
            memory_resonance=metrics.get('memory_imprints', 0)
        )
        
        self.state.resonance_history.append(snapshot)
        
        # Update total incubation time
        if 'time_spent' in metrics:
            self.state.total_incubation_time += metrics['time_spent']

        # Check all active incubations for progress
        for incubation in self.state.active_incubations:
            self.update_incubation_progress(incubation, metrics)

        # Check for stage completions
        self.check_stage_completions()
        
        # Notify observers
        self.notify_progress_callbacks()

    def update_incubation_progress(self, incubation: ActiveIncubation, metrics: Dict[str, Any]):
        """Update progress for a specific incubation"""
        stage = next((s for s in INCUBATION_STAGES if s.id == incubation.stage_id), None)
        if not stage:
            return

        for trigger in incubation.current_triggers:
            if trigger.type == 'coherence' and metrics.get('coherence', 0) >= trigger.threshold:
                trigger.completed = True
            elif trigger.type == 'gate_activation' and metrics.get('active_gates', 0) >= trigger.threshold:
                trigger.completed = True
            elif trigger.type == 'memory_resonance' and metrics.get('memory_imprints', 0) >= trigger.threshold:
                trigger.completed = True
            elif trigger.type == 'waveform_stability' and metrics.get('waveform_stability', 0) >= trigger.threshold:
                trigger.completed = True
            elif trigger.type == 'glyph_combination' and metrics.get('glyph_combinations', 0) >= trigger.threshold:
                trigger.completed = True
            elif trigger.type == 'time_spent' and self.state.total_incubation_time >= trigger.threshold:
                trigger.completed = True

        # Calculate overall progress
        completed_triggers = sum(1 for t in incubation.current_triggers if t.completed)
        incubation.progress_percent = (completed_triggers / len(incubation.current_triggers)) * 100
        incubation.is_ready = incubation.progress_percent == 100

    def check_stage_completions(self):
        """Check for completed stages and apply rewards"""
        completed_incubations = []
        for i, incubation in enumerate(self.state.active_incubations):
            if incubation.is_ready and incubation.stage_id not in self.state.completed_stages:
                self.complete_stage(incubation.stage_id)
                completed_incubations.append(i)

        # Remove completed incubations (in reverse order to maintain indices)
        for i in reversed(completed_incubations):
            self.state.active_incubations.pop(i)

    def complete_stage(self, stage_id: str):
        """Complete a stage and apply rewards"""
        stage = next((s for s in INCUBATION_STAGES if s.id == stage_id), None)
        if not stage:
            return

        self.state.completed_stages.append(stage_id)
        
        # Apply rewards
        for reward in stage.rewards:
            self.apply_reward(reward)

        # Update field maturity
        self.state.field_maturity = min(100, self.state.field_maturity + 15)

        # Auto-start next stage if available
        current_index = next((i for i, s in enumerate(INCUBATION_STAGES) if s.id == stage_id), -1)
        if current_index >= 0 and current_index + 1 < len(INCUBATION_STAGES):
            next_stage = INCUBATION_STAGES[current_index + 1]
            if self.can_start_stage(next_stage):
                self.state.current_stage = next_stage.id

    def apply_reward(self, reward: IncubationReward):
        """Apply incubation rewards to the field system"""
        print(f"Applying reward: {reward.description} ({reward.value})")
        # Integration points for your existing systems:
        # - field_expansion: Update field sensitivity
        # - new_trait_unlock: Enable new features
        # - resonance_boost: Enhance calculations
        # - memory_capacity: Expand memory limits
        # - glyph_access: Unlock new combinations

    def can_start_stage(self, stage: IncubationStage) -> bool:
        """Check if prerequisites are met for a stage"""
        current_metrics = self.get_current_metrics()
        return (
            current_metrics['coherence'] >= stage.required_coherence and
            current_metrics['active_gates'] >= stage.required_gate_activations and
            current_metrics['memory_imprints'] >= stage.required_memory_imprints
        )

    def get_current_metrics(self) -> Dict[str, float]:
        """Get current field metrics"""
        if not self.state.resonance_history:
            return {'coherence': 0, 'active_gates': 0, 'memory_imprints': 0}
        
        latest = self.state.resonance_history[-1]
        return {
            'coherence': latest.coherence_level,
            'active_gates': latest.active_gates,
            'memory_imprints': latest.memory_resonance
        }

    def generate_waveform_pattern(self, metrics: Dict[str, Any]) -> str:
        """Generate a waveform pattern based on current metrics"""
        coherence = metrics.get('coherence', 0)
        if coherence >= 80:
            return "HARMONIC_RESONANCE"
        elif coherence >= 60:
            return "STABLE_OSCILLATION"
        elif coherence >= 40:
            return "DEVELOPING_PATTERN"
        else:
            return "EMERGENT_FIELD"

    def add_progress_callback(self, callback: Callable):
        """Add a callback for progress updates"""
        self.progress_callbacks.append(callback)

    def notify_progress_callbacks(self):
        """Notify all registered callbacks of state changes"""
        for callback in self.progress_callbacks:
            try:
                callback(self.state)
            except Exception as e:
                print(f"Error in progress callback: {e}")

    def get_state_dict(self) -> Dict:
        """Get serializable state dictionary"""
        return {
            'user_id': self.state.user_id,
            'current_stage': self.state.current_stage,
            'field_maturity': self.state.field_maturity,
            'total_incubation_time': self.state.total_incubation_time,
            'completed_stages': self.state.completed_stages,
            'active_incubations_count': len(self.state.active_incubations),
            'resonance_history_count': len(self.state.resonance_history)
        }

    def get_available_stages(self) -> List[Dict]:
        """Get list of available stages with their status"""
        stages_info = []
        for stage in INCUBATION_STAGES:
            can_start = self.can_start_stage(stage)
            is_completed = stage.id in self.state.completed_stages
            is_active = any(inc.stage_id == stage.id for inc in self.state.active_incubations)
            
            stages_info.append({
                'id': stage.id,
                'name': stage.name,
                'description': stage.description,
                'can_start': can_start,
                'is_completed': is_completed,
                'is_active': is_active,
                'duration_hours': stage.duration
            })
        
        return stages_info
