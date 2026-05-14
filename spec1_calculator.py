
"""
YOU-N-I-VERSE Core Engine: spec1_calculator.py
Trinity Chart Generator - Gate.Line.Color.Tone.Base Calculator

Converts birth data into the 5-layer consciousness map that powers
the entire YOU-N-I-VERSE system.
"""

import math
from datetime import datetime, timezone
from typing import Dict, Tuple, Any
import json
from gate_codon_mapper import CompleteGateCodonMapper, enhance_trinity_chart_with_biological_layers

class TrinityChartCalculator:
    """
    Core engine for calculating Gate.Line.Color.Tone.Base from birth data.
    This is the atomic structure of consciousness in YOU-N-I-VERSE.
    """
    
    def __init__(self):
        # Human Design gate wheel (64 gates mapped to zodiac degrees)
        self.gate_wheel = self._initialize_gate_wheel()
        
        # Codon mapping (64 DNA codons to 64 gates)
        self.codon_map = self._initialize_codon_map()
        
        # Color/Tone/Base progression rules
        self.color_names = ["Fear", "Hope", "Desire", "Need", "Guilt", "Innocence"]
        self.tone_names = ["Security", "Taste", "Outer Vision", "Meditation", "Judgment", "Acceptance"]
        self.base_names = ["Left", "Right", "Receptive", "Projective"]
    
    def _initialize_gate_wheel(self) -> Dict[int, float]:
        """Initialize the 64-gate wheel mapped to zodiac degrees."""
        gate_wheel = {}
        degree_per_gate = 360 / 64  # ~5.625 degrees per gate
        
        # Start at 0° Aries (gate order follows I'Ching sequence)
        rave_order = [
            41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
            27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
            31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
            28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60
        ]
        
        for i, gate in enumerate(rave_order):
            gate_wheel[gate] = i * degree_per_gate
            
        return gate_wheel
    
    def _initialize_codon_map(self) -> Dict[int, str]:
        """Map each gate to its corresponding DNA codon."""
        # Simplified codon mapping (in real implementation, use full genetic code)
        codons = [
            "TTT", "TTC", "TTA", "TTG", "TCT", "TCC", "TCA", "TCG",
            "TAT", "TAC", "TAA", "TAG", "TGT", "TGC", "TGA", "TGG",
            "CTT", "CTC", "CTA", "CTG", "CCT", "CCC", "CCA", "CCG",
            "CAT", "CAC", "CAA", "CAG", "CGT", "CGC", "CGA", "CGG",
            "ATT", "ATC", "ATA", "ATG", "ACT", "ACC", "ACA", "ACG",
            "AAT", "AAC", "AAA", "AAG", "AGT", "AGC", "AGA", "AGG",
            "GTT", "GTC", "GTA", "GTG", "GCT", "GCC", "GCA", "GCG",
            "GAT", "GAC", "GAA", "GAG", "GGT", "GGC", "GGA", "GGG"
        ]
        
        return {i+1: codons[i] for i in range(64)}
    
    def calculate_sun_position(self, birth_datetime: datetime, latitude: float, longitude: float) -> float:
        """
        Calculate sun position in zodiac degrees.
        Simplified calculation - in production use proper astronomical library.
        """
        # Days since J2000.0 epoch
        j2000 = datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        days_since_j2000 = (birth_datetime - j2000).total_seconds() / 86400
        
        # Mean longitude of sun (simplified)
        L = (280.460 + 0.9856474 * days_since_j2000) % 360
        
        # Mean anomaly
        g = math.radians((357.528 + 0.9856003 * days_since_j2000) % 360)
        
        # Ecliptic longitude (simplified equation of center)
        sun_longitude = (L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g)) % 360
        
        return sun_longitude
    
    def degree_to_gate_line(self, degree: float) -> Tuple[int, int]:
        """Convert zodiac degree to Gate and Line."""
        # Find which gate this degree falls into
        degree_per_gate = 360 / 64
        degree_per_line = degree_per_gate / 6  # 6 lines per gate
        
        gate_index = int(degree / degree_per_gate)
        gate = list(self.gate_wheel.keys())[gate_index]
        
        # Calculate line within the gate
        degree_in_gate = degree % degree_per_gate
        line = int(degree_in_gate / degree_per_line) + 1
        line = min(line, 6)  # Ensure line is 1-6
        
        return gate, line
    
    def calculate_color_tone_base(self, degree: float, time_of_day: datetime) -> Tuple[int, int, int]:
        """
        Calculate Color, Tone, and Base from precise degree and time.
        This is where the quantum precision happens.
        """
        # Color: based on 60-degree segments (6 colors per gate cycle)
        degree_per_color = 360 / 64 / 6  # ~0.9375 degrees per color
        color = int((degree % (360/64)) / degree_per_color) + 1
        color = min(color, 6)
        
        # Tone: based on minutes of birth time (6 tones, ~10 minutes each)
        minutes_in_hour = time_of_day.minute
        tone = int(minutes_in_hour / 10) + 1
        tone = min(tone, 6)
        
        # Base: based on seconds and hemispheric resonance (4 bases)
        seconds = time_of_day.second
        base = int(seconds / 15) + 1  # 15-second intervals
        base = min(base, 4)
        
        return color, tone, base
    
    def generate_trinity_chart(self, 
                             birth_datetime: datetime,
                             latitude: float = 0.0,
                             longitude: float = 0.0) -> Dict[str, Any]:
        """
        Generate complete Trinity Chart from birth data.
        This is the consciousness DNA that powers everything.
        """
        # Calculate sun position
        sun_degree = self.calculate_sun_position(birth_datetime, latitude, longitude)
        
        # Get Gate and Line
        gate, line = self.degree_to_gate_line(sun_degree)
        
        # Get Color, Tone, Base
        color, tone, base = self.calculate_color_tone_base(sun_degree, birth_datetime)
        
        # Get corresponding codon
        codon = self.codon_map.get(gate, "UNK")
        
        # Build the complete chart
        trinity_chart = {
            "birth_data": {
                "datetime": birth_datetime.isoformat(),
                "latitude": latitude,
                "longitude": longitude
            },
            "sun_position": {
                "degree": round(sun_degree, 6),
                "gate": gate,
                "line": line,
                "color": color,
                "tone": tone,
                "base": base
            },
            "genetic_code": {
                "codon": codon,
                "gate_codon": f"Gate {gate} - {codon}"
            },
            "resonance_signature": {
                "core_identity": f"{gate}.{line}",
                "quantum_structure": f"{gate}.{line}.{color}.{tone}.{base}",
                "color_name": self.color_names[color-1],
                "tone_name": self.tone_names[tone-1],
                "base_name": self.base_names[base-1]
            },
            "field_coordinates": {
                "x": gate,
                "y": line,
                "z": color,
                "t": tone,
                "d": base
            }
        }
        
        # Enhance with biological resonance layers
        trinity_chart = enhance_trinity_chart_with_biological_layers(trinity_chart)
        
        return trinity_chart
    
    def chart_to_field_seed(self, chart: Dict[str, Any]) -> str:
        """
        Convert chart to a field seed string for AI personality generation.
        This becomes the DNA for Field Friends and Cynthia.
        """
        pos = chart["sun_position"]
        field_seed = f"{pos['gate']}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}"
        return field_seed
    
    def calculate_resonance_compatibility(self, chart1: Dict, chart2: Dict) -> float:
        """
        Calculate resonance compatibility between two charts.
        Used for Field Friend bonding and user matching.
        """
        pos1 = chart1["sun_position"]
        pos2 = chart2["sun_position"]
        
        # Gate harmony (complementary or same)
        gate_diff = abs(pos1["gate"] - pos2["gate"])
        gate_score = 1.0 if gate_diff == 0 else 1.0 / (1 + gate_diff / 64)
        
        # Line resonance
        line_score = 1.0 - abs(pos1["line"] - pos2["line"]) / 6
        
        # Color/Tone/Base micro-resonance
        color_score = 1.0 - abs(pos1["color"] - pos2["color"]) / 6
        tone_score = 1.0 - abs(pos1["tone"] - pos2["tone"]) / 6
        base_score = 1.0 - abs(pos1["base"] - pos2["base"]) / 4
        
        # Weighted compatibility
        compatibility = (
            gate_score * 0.4 +
            line_score * 0.3 +
            color_score * 0.15 +
            tone_score * 0.1 +
            base_score * 0.05
        )
        
        return round(compatibility, 3)


# Legacy compatibility function for existing endpoints
def calculate_gate_line_color_tone_base(birth_date, birth_time, location):
    """
    Legacy compatibility function - converts to new Trinity system format
    """
    calculator = TrinityChartCalculator()
    
    # Parse birth data
    birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    
    # Generate full trinity chart
    chart = calculator.generate_trinity_chart(birth_datetime, 0.0, 0.0)
    
    # Convert to legacy format for existing endpoints
    pos = chart["sun_position"]
    legacy_format = {
        "Sun": f"{pos['gate']}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Earth": f"{(pos['gate'] + 31) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Moon": f"{(pos['gate'] + 15) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "North_Node": f"{(pos['gate'] + 7) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "South_Node": f"{(pos['gate'] + 39) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Mercury": f"{(pos['gate'] + 3) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Venus": f"{(pos['gate'] + 23) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Mars": f"{(pos['gate'] + 11) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Jupiter": f"{(pos['gate'] + 47) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "Saturn": f"{(pos['gate'] + 19) % 64 + 1}.{pos['line']}.{pos['color']}.{pos['tone']}.{pos['base']}",
        "trinity_chart": chart,  # Include full trinity chart
        "birth_info": {
            "date": birth_date,
            "time": birth_time,
            "location": location
        }
    }
    
    return legacy_format


# Example usage and testing
if __name__ == "__main__":
    # Initialize calculator
    calc = TrinityChartCalculator()
    
    # Example birth data
    birth_time = datetime(1990, 6, 15, 14, 30, 45)  # June 15, 1990, 2:30:45 PM
    latitude = 37.7749  # San Francisco
    longitude = -122.4194
    
    # Generate Trinity Chart
    chart = calc.generate_trinity_chart(birth_time, latitude, longitude)
    
    # Display results
    print("🌌 YOU-N-I-VERSE Trinity Chart Generated:")
    print(f"Field Signature: {chart['resonance_signature']['quantum_structure']}")
    print(f"Codon: {chart['genetic_code']['codon']}")
    print(f"Resonance: {chart['resonance_signature']['color_name']} • {chart['resonance_signature']['tone_name']} • {chart['resonance_signature']['base_name']}")
    print(f"Field Seed: {calc.chart_to_field_seed(chart)}")
    
    # Test compatibility with another chart
    chart2 = calc.generate_trinity_chart(datetime(1985, 12, 3, 8, 15, 20))
    compatibility = calc.calculate_resonance_compatibility(chart, chart2)
    print(f"Resonance Compatibility: {compatibility * 100:.1f}%")
