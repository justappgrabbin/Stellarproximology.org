
# ==================================================
# COMPLETE GATE→CODON→ELEMENT→FIELD RESONANCE SYSTEM
# Full 64-gate mapping with biological and elemental resonance
# ==================================================

import json
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

class CompleteGateCodonMapper:
    """
    Complete mapping system connecting Human Design gates to genetic codons,
    amino acids, elements, field types, and symbolic overlays.
    """
    
    def __init__(self):
        # COMPLETE 64-GATE MAPPING (Ra Uru Hu's system + biological resonance)
        self.COMPLETE_GATE_MAP = {
            1:  {"codon": "GGC", "amino_acid": "Glycine",         "element": "Carbon",     "field": "Creative Power",      "symbol": "Judah",     "tribe_energy": "Leadership"},
            2:  {"codon": "CCC", "amino_acid": "Proline",         "element": "Nitrogen",   "field": "Receptive Direction",  "symbol": "Issachar",  "tribe_energy": "Wisdom"},
            3:  {"codon": "GGA", "amino_acid": "Glycine",         "element": "Carbon",     "field": "Ordering Mutation",    "symbol": "Naphtali",  "tribe_energy": "Innovation"},
            4:  {"codon": "CGC", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Mental Logic",         "symbol": "Reuben",    "tribe_energy": "Answers"},
            5:  {"codon": "GGT", "amino_acid": "Glycine",         "element": "Carbon",     "field": "Fixed Rhythms",        "symbol": "Levi",      "tribe_energy": "Timing"},
            6:  {"codon": "CAG", "amino_acid": "Glutamine",       "element": "Nitrogen",   "field": "Emotional Friction",   "symbol": "Simeon",    "tribe_energy": "Intimacy"},
            7:  {"codon": "TGG", "amino_acid": "Tryptophan",      "element": "Carbon",     "field": "Leadership Role",      "symbol": "Gad",       "tribe_energy": "Guidance"},
            8:  {"codon": "GGG", "amino_acid": "Glycine",         "element": "Carbon",     "field": "Individual Contribution", "symbol": "Dan",    "tribe_energy": "Uniqueness"},
            9:  {"codon": "TGT", "amino_acid": "Cysteine",        "element": "Sulfur",     "field": "Focused Determination", "symbol": "Asher",   "tribe_energy": "Energy"},
            10: {"codon": "CAC", "amino_acid": "Histidine",       "element": "Nitrogen",   "field": "Self Behavior",        "symbol": "Zebulun",   "tribe_energy": "Authenticity"},
            11: {"codon": "GAC", "amino_acid": "Aspartic Acid",   "element": "Oxygen",     "field": "Peaceful Ideas",       "symbol": "Joseph",    "tribe_energy": "Harmony"},
            12: {"codon": "GAG", "amino_acid": "Glutamic Acid",   "element": "Oxygen",     "field": "Artistic Channel",     "symbol": "Benjamin",  "tribe_energy": "Expression"},
            13: {"codon": "GAT", "amino_acid": "Aspartic Acid",   "element": "Oxygen",     "field": "Fellowship Listener",  "symbol": "Manasseh",  "tribe_energy": "Community"},
            14: {"codon": "TTG", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Power Skills",         "symbol": "Ephraim",   "tribe_energy": "Mastery"},
            15: {"codon": "CTG", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Extreme Modesty",      "symbol": "Dinah",     "tribe_energy": "Balance"},
            16: {"codon": "TGC", "amino_acid": "Cysteine",        "element": "Sulfur",     "field": "Enthusiastic Skills",  "symbol": "Judah",     "tribe_energy": "Talent"},
            17: {"codon": "AGA", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Following Opinions",   "symbol": "Issachar",  "tribe_energy": "Service"},
            18: {"codon": "CGG", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Corrective Work",      "symbol": "Naphtali",  "tribe_energy": "Healing"},
            19: {"codon": "AAT", "amino_acid": "Asparagine",      "element": "Nitrogen",   "field": "Wanting Approach",     "symbol": "Reuben",    "tribe_energy": "Need"},
            20: {"codon": "AAC", "amino_acid": "Asparagine",      "element": "Nitrogen",   "field": "Present Contemplation", "symbol": "Levi",     "tribe_energy": "Awareness"},
            21: {"codon": "AGG", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Biting Control",       "symbol": "Simeon",    "tribe_energy": "Will"},
            22: {"codon": "TAT", "amino_acid": "Tyrosine",        "element": "Oxygen",     "field": "Graceful Openness",    "symbol": "Gad",       "tribe_energy": "Beauty"},
            23: {"codon": "ATA", "amino_acid": "Isoleucine",      "element": "Carbon",     "field": "Splitting Assimilation", "symbol": "Dan",     "tribe_energy": "Insight"},
            24: {"codon": "TTA", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Returning Blessing",   "symbol": "Asher",     "tribe_energy": "Renewal"},
            25: {"codon": "TAA", "amino_acid": "Stop Codon",      "element": "Void",       "field": "Universal Love",       "symbol": "Zebulun",   "tribe_energy": "Spirit"},
            26: {"codon": "GTA", "amino_acid": "Valine",          "element": "Carbon",     "field": "Great Taming",         "symbol": "Joseph",    "tribe_energy": "Accumulation"},
            27: {"codon": "ATT", "amino_acid": "Isoleucine",      "element": "Carbon",     "field": "Caring Nourishment",   "symbol": "Benjamin",  "tribe_energy": "Responsibility"},
            28: {"codon": "TCA", "amino_acid": "Serine",          "element": "Oxygen",     "field": "Great Struggle",       "symbol": "Manasseh",  "tribe_energy": "Purpose"},
            29: {"codon": "GAA", "amino_acid": "Glutamic Acid",   "element": "Oxygen",     "field": "Abyssal Commitment",   "symbol": "Ephraim",   "tribe_energy": "Perseverance"},
            30: {"codon": "GTG", "amino_acid": "Valine",          "element": "Carbon",     "field": "Clinging Feelings",    "symbol": "Dinah",     "tribe_energy": "Clarity"},
            31: {"codon": "TAC", "amino_acid": "Tyrosine",        "element": "Oxygen",     "field": "Leading Influence",    "symbol": "Judah",     "tribe_energy": "Attraction"},
            32: {"codon": "CAT", "amino_acid": "Histidine",       "element": "Nitrogen",   "field": "Enduring Continuity",  "symbol": "Issachar",  "tribe_energy": "Conservation"},
            33: {"codon": "TGA", "amino_acid": "Stop Codon",      "element": "Void",       "field": "Private Retreat",      "symbol": "Naphtali",  "tribe_energy": "Withdrawal"},
            34: {"codon": "TCT", "amino_acid": "Serine",          "element": "Oxygen",     "field": "Great Power",          "symbol": "Reuben",    "tribe_energy": "Strength"},
            35: {"codon": "GCT", "amino_acid": "Alanine",         "element": "Carbon",     "field": "Progressive Change",   "symbol": "Levi",      "tribe_energy": "Experience"},
            36: {"codon": "AGT", "amino_acid": "Serine",          "element": "Oxygen",     "field": "Darkening Crisis",     "symbol": "Simeon",    "tribe_energy": "Exploration"},
            37: {"codon": "TTC", "amino_acid": "Phenylalanine",   "element": "Carbon",     "field": "Family Friendship",    "symbol": "Gad",       "tribe_energy": "Community"},
            38: {"codon": "ACT", "amino_acid": "Threonine",       "element": "Oxygen",     "field": "Opposition Fighter",   "symbol": "Dan",       "tribe_energy": "Individuality"},
            39: {"codon": "GCA", "amino_acid": "Alanine",         "element": "Carbon",     "field": "Provocative Obstruction", "symbol": "Asher",  "tribe_energy": "Spirit"},
            40: {"codon": "GCG", "amino_acid": "Alanine",         "element": "Carbon",     "field": "Alone Deliverance",    "symbol": "Zebulun",   "tribe_energy": "Forgiveness"},
            41: {"codon": "TTT", "amino_acid": "Phenylalanine",   "element": "Carbon",     "field": "Decrease Contraction", "symbol": "Joseph",    "tribe_energy": "Imagination"},
            42: {"codon": "CTT", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Increase Growth",      "symbol": "Benjamin",  "tribe_energy": "Completion"},
            43: {"codon": "TCC", "amino_acid": "Serine",          "element": "Oxygen",     "field": "Breakthrough Insight", "symbol": "Manasseh",  "tribe_energy": "Individual"},
            44: {"codon": "CAA", "amino_acid": "Glutamine",       "element": "Nitrogen",   "field": "Coming Truth",         "symbol": "Ephraim",   "tribe_energy": "Recognition"},
            45: {"codon": "ATG", "amino_acid": "Methionine",      "element": "Sulfur",     "field": "Gathering Ruler",      "symbol": "Dinah",     "tribe_energy": "Education"},
            46: {"codon": "CTC", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Upward Determination", "symbol": "Judah",     "tribe_energy": "Seriousness"},
            47: {"codon": "CGA", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Oppressive Realization", "symbol": "Issachar", "tribe_energy": "Understanding"},
            48: {"codon": "TGT", "amino_acid": "Cysteine",        "element": "Sulfur",     "field": "Well Depth",           "symbol": "Naphtali",  "tribe_energy": "Wisdom"},
            49: {"codon": "GTT", "amino_acid": "Valine",          "element": "Carbon",     "field": "Revolutionary Principles", "symbol": "Reuben", "tribe_energy": "Change"},
            50: {"codon": "CGT", "amino_acid": "Arginine",        "element": "Nitrogen",   "field": "Cauldron Values",      "symbol": "Levi",      "tribe_energy": "Responsibility"},
            51: {"codon": "AAG", "amino_acid": "Lysine",          "element": "Nitrogen",   "field": "Arousing Shock",       "symbol": "Simeon",    "tribe_energy": "Initiation"},
            52: {"codon": "AAC", "amino_acid": "Asparagine",      "element": "Nitrogen",   "field": "Still Mountain",       "symbol": "Gad",       "tribe_energy": "Concentration"},
            53: {"codon": "ACC", "amino_acid": "Threonine",       "element": "Oxygen",     "field": "Gradual Development",  "symbol": "Dan",       "tribe_energy": "Maturation"},
            54: {"codon": "TAC", "amino_acid": "Tyrosine",        "element": "Oxygen",     "field": "Marrying Ambition",    "symbol": "Asher",     "tribe_energy": "Drive"},
            55: {"codon": "AGC", "amino_acid": "Serine",          "element": "Oxygen",     "field": "Abundant Spirit",      "symbol": "Zebulun",   "tribe_energy": "Freedom"},
            56: {"codon": "GTG", "amino_acid": "Valine",          "element": "Carbon",     "field": "Wandering Stimulation", "symbol": "Joseph",   "tribe_energy": "Diversity"},
            57: {"codon": "CCA", "amino_acid": "Proline",         "element": "Nitrogen",   "field": "Gentle Intuition",     "symbol": "Benjamin",  "tribe_energy": "Clarity"},
            58: {"codon": "AAT", "amino_acid": "Asparagine",      "element": "Nitrogen",   "field": "Joyous Vitality",      "symbol": "Manasseh",  "tribe_energy": "Joy"},
            59: {"codon": "GAG", "amino_acid": "Glutamic Acid",   "element": "Oxygen",     "field": "Dispersing Sexuality", "symbol": "Ephraim",   "tribe_energy": "Dispersion"},
            60: {"codon": "AAG", "amino_acid": "Lysine",          "element": "Nitrogen",   "field": "Accepting Limitation", "symbol": "Dinah",     "tribe_energy": "Restriction"},
            61: {"codon": "GGA", "amino_acid": "Glycine",         "element": "Carbon",     "field": "Inner Truth Mystery",  "symbol": "Judah",     "tribe_energy": "Knowledge"},
            62: {"codon": "GCG", "amino_acid": "Alanine",         "element": "Carbon",     "field": "Detailed Precision",   "symbol": "Issachar",  "tribe_energy": "Small"},
            63: {"codon": "TAG", "amino_acid": "Stop Codon",      "element": "Void",       "field": "Doubtful Completion",  "symbol": "Naphtali",  "tribe_energy": "Inquiry"},
            64: {"codon": "CTG", "amino_acid": "Leucine",         "element": "Carbon",     "field": "Confused Before",      "symbol": "Reuben",    "tribe_energy": "Imagination"}
        }
        
        # Element resonance properties
        self.ELEMENT_PROPERTIES = {
            "Carbon": {
                "type": "structural",
                "energy": "building",
                "vibration": "foundation",
                "consciousness": "form",
                "sacred_geometry": "cube"
            },
            "Nitrogen": {
                "type": "mental",
                "energy": "thinking",
                "vibration": "expansion",
                "consciousness": "mind",
                "sacred_geometry": "tetrahedron"
            },
            "Oxygen": {
                "type": "emotional",
                "energy": "flowing",
                "vibration": "circulation",
                "consciousness": "feeling",
                "sacred_geometry": "octahedron"
            },
            "Sulfur": {
                "type": "transformational",
                "energy": "alchemical",
                "vibration": "mutation",
                "consciousness": "transmutation",
                "sacred_geometry": "dodecahedron"
            },
            "Void": {
                "type": "transcendent",
                "energy": "completion",
                "vibration": "silence",
                "consciousness": "void",
                "sacred_geometry": "sphere"
            }
        }
        
        # Tribal energy frequencies
        self.TRIBAL_FREQUENCIES = {
            "Judah": {"frequency": "leadership", "color": "gold", "tone": "commanding"},
            "Issachar": {"frequency": "wisdom", "color": "blue", "tone": "understanding"},
            "Naphtali": {"frequency": "swiftness", "color": "silver", "tone": "agile"},
            "Reuben": {"frequency": "strength", "color": "red", "tone": "powerful"},
            "Levi": {"frequency": "service", "color": "white", "tone": "devotional"},
            "Simeon": {"frequency": "hearing", "color": "green", "tone": "receptive"},
            "Gad": {"frequency": "fortune", "color": "purple", "tone": "abundant"},
            "Dan": {"frequency": "judgment", "color": "indigo", "tone": "discerning"},
            "Asher": {"frequency": "happiness", "color": "orange", "tone": "joyful"},
            "Zebulun": {"frequency": "dwelling", "color": "cyan", "tone": "stable"},
            "Joseph": {"frequency": "increase", "color": "rainbow", "tone": "multiplying"},
            "Benjamin": {"frequency": "beloved", "color": "pink", "tone": "cherished"},
            "Manasseh": {"frequency": "forgetting", "color": "grey", "tone": "releasing"},
            "Ephraim": {"frequency": "fruitful", "color": "emerald", "tone": "creative"},
            "Dinah": {"frequency": "judgment", "color": "violet", "tone": "balancing"}
        }
        
    def get_complete_gate_metadata(self, gate_number: int) -> Dict[str, Any]:
        """Get complete metadata for a gate including all resonance layers."""
        
        if gate_number not in self.COMPLETE_GATE_MAP:
            return self._get_default_metadata(gate_number)
        
        gate_data = self.COMPLETE_GATE_MAP[gate_number]
        element = gate_data["element"]
        symbol = gate_data["symbol"]
        
        complete_metadata = {
            "gate": gate_number,
            "codon": gate_data["codon"],
            "amino_acid": gate_data["amino_acid"],
            "element": element,
            "field_type": gate_data["field"],
            "tribal_symbol": symbol,
            "tribal_energy": gate_data["tribe_energy"],
            "element_properties": self.ELEMENT_PROPERTIES.get(element, {}),
            "tribal_frequency": self.TRIBAL_FREQUENCIES.get(symbol, {}),
            "resonance_signature": f"{gate_number}-{gate_data['codon']}-{element}",
            "consciousness_layer": self._determine_consciousness_layer(element),
            "field_activation": self._generate_field_activation(gate_data),
            "molecular_structure": self._get_molecular_info(gate_data["amino_acid"]),
            "sacred_geometry": self.ELEMENT_PROPERTIES.get(element, {}).get("sacred_geometry", "sphere")
        }
        
        return complete_metadata
    
    def _get_default_metadata(self, gate_number: int) -> Dict[str, Any]:
        """Default metadata for unmapped gates."""
        return {
            "gate": gate_number,
            "codon": "UNK",
            "amino_acid": "Unknown",
            "element": "Void",
            "field_type": "Mystery",
            "tribal_symbol": "Unknown",
            "tribal_energy": "Hidden",
            "element_properties": self.ELEMENT_PROPERTIES["Void"],
            "tribal_frequency": {"frequency": "mystery", "color": "black", "tone": "silent"},
            "resonance_signature": f"{gate_number}-UNK-Void",
            "consciousness_layer": "transcendent",
            "field_activation": "dormant",
            "molecular_structure": {"bonds": 0, "structure": "unknown"},
            "sacred_geometry": "void"
        }
    
    def _determine_consciousness_layer(self, element: str) -> str:
        """Determine consciousness layer based on element."""
        
        layer_map = {
            "Carbon": "form_consciousness",
            "Nitrogen": "mental_consciousness", 
            "Oxygen": "emotional_consciousness",
            "Sulfur": "transformational_consciousness",
            "Void": "transcendent_consciousness"
        }
        
        return layer_map.get(element, "form_consciousness")
    
    def _generate_field_activation(self, gate_data: Dict[str, Any]) -> str:
        """Generate field activation pattern based on gate data."""
        
        element = gate_data["element"]
        field_type = gate_data["field"]
        
        activation_patterns = {
            "Carbon": f"Building {field_type.lower()} through structural alignment",
            "Nitrogen": f"Thinking {field_type.lower()} through mental expansion", 
            "Oxygen": f"Feeling {field_type.lower()} through emotional flow",
            "Sulfur": f"Transforming {field_type.lower()} through alchemical mutation",
            "Void": f"Transcending {field_type.lower()} through cosmic completion"
        }
        
        return activation_patterns.get(element, f"Activating {field_type.lower()}")
    
    def _get_molecular_info(self, amino_acid: str) -> Dict[str, Any]:
        """Get molecular structure information for amino acid."""
        
        molecular_info = {
            "Glycine": {"bonds": 4, "structure": "simple", "polarity": "nonpolar"},
            "Proline": {"bonds": 5, "structure": "cyclic", "polarity": "nonpolar"},
            "Arginine": {"bonds": 6, "structure": "basic", "polarity": "charged"},
            "Glutamine": {"bonds": 5, "structure": "amide", "polarity": "polar"},
            "Tryptophan": {"bonds": 11, "structure": "aromatic", "polarity": "nonpolar"},
            "Cysteine": {"bonds": 3, "structure": "sulfur", "polarity": "polar"},
            "Histidine": {"bonds": 6, "structure": "imidazole", "polarity": "charged"},
            "Aspartic Acid": {"bonds": 4, "structure": "acidic", "polarity": "charged"},
            "Glutamic Acid": {"bonds": 5, "structure": "acidic", "polarity": "charged"},
            "Leucine": {"bonds": 6, "structure": "branched", "polarity": "nonpolar"},
            "Asparagine": {"bonds": 4, "structure": "amide", "polarity": "polar"},
            "Tyrosine": {"bonds": 9, "structure": "aromatic", "polarity": "polar"},
            "Isoleucine": {"bonds": 6, "structure": "branched", "polarity": "nonpolar"},
            "Stop Codon": {"bonds": 0, "structure": "terminal", "polarity": "void"},
            "Valine": {"bonds": 5, "structure": "branched", "polarity": "nonpolar"},
            "Serine": {"bonds": 3, "structure": "hydroxyl", "polarity": "polar"},
            "Alanine": {"bonds": 4, "structure": "simple", "polarity": "nonpolar"},
            "Phenylalanine": {"bonds": 9, "structure": "aromatic", "polarity": "nonpolar"},
            "Threonine": {"bonds": 4, "structure": "hydroxyl", "polarity": "polar"},
            "Methionine": {"bonds": 5, "structure": "sulfur", "polarity": "nonpolar"},
            "Lysine": {"bonds": 6, "structure": "basic", "polarity": "charged"},
            "Unknown": {"bonds": 0, "structure": "unknown", "polarity": "neutral"}
        }
        
        return molecular_info.get(amino_acid, {"bonds": 0, "structure": "unknown", "polarity": "neutral"})
    
    def analyze_gate_combination(self, gates: List[int]) -> Dict[str, Any]:
        """Analyze a combination of gates for resonance patterns."""
        
        if not gates:
            return {"error": "No gates provided"}
        
        gate_metadatas = [self.get_complete_gate_metadata(gate) for gate in gates]
        
        # Element distribution
        elements = [gm["element"] for gm in gate_metadatas]
        element_counts = {elem: elements.count(elem) for elem in set(elements)}
        
        # Consciousness layer distribution  
        consciousness_layers = [gm["consciousness_layer"] for gm in gate_metadatas]
        layer_counts = {layer: consciousness_layers.count(layer) for layer in set(consciousness_layers)}
        
        # Tribal energy distribution
        tribal_energies = [gm["tribal_energy"] for gm in gate_metadatas]
        energy_counts = {energy: tribal_energies.count(energy) for energy in set(tribal_energies)}
        
        # Dominant patterns
        dominant_element = max(element_counts, key=element_counts.get)
        dominant_consciousness = max(layer_counts, key=layer_counts.get)
        dominant_energy = max(energy_counts, key=energy_counts.get)
        
        # Field activation synthesis
        field_synthesis = self._synthesize_field_activations(gate_metadatas)
        
        return {
            "gates_analyzed": gates,
            "total_gates": len(gates),
            "element_distribution": element_counts,
            "consciousness_distribution": layer_counts,
            "tribal_energy_distribution": energy_counts,
            "dominant_patterns": {
                "element": dominant_element,
                "consciousness": dominant_consciousness,
                "tribal_energy": dominant_energy
            },
            "field_synthesis": field_synthesis,
            "resonance_score": self._calculate_resonance_score(gate_metadatas),
            "molecular_complexity": sum(gm["molecular_structure"]["bonds"] for gm in gate_metadatas),
            "gate_details": gate_metadatas
        }
    
    def _synthesize_field_activations(self, gate_metadatas: List[Dict[str, Any]]) -> str:
        """Synthesize field activations into a unified pattern."""
        
        activations = [gm["field_activation"] for gm in gate_metadatas]
        
        # Extract common patterns
        building_count = sum(1 for a in activations if "Building" in a)
        thinking_count = sum(1 for a in activations if "Thinking" in a)
        feeling_count = sum(1 for a in activations if "Feeling" in a)
        transforming_count = sum(1 for a in activations if "Transforming" in a)
        transcending_count = sum(1 for a in activations if "Transcending" in a)
        
        if building_count >= thinking_count and building_count >= feeling_count:
            return f"Primary field activation: Structural building with {building_count} building patterns"
        elif thinking_count >= feeling_count:
            return f"Primary field activation: Mental expansion with {thinking_count} thinking patterns"
        elif feeling_count > 0:
            return f"Primary field activation: Emotional flow with {feeling_count} feeling patterns"
        elif transforming_count > 0:
            return f"Primary field activation: Alchemical transformation with {transforming_count} transforming patterns"
        else:
            return f"Primary field activation: Transcendent completion with {transcending_count} transcending patterns"
    
    def _calculate_resonance_score(self, gate_metadatas: List[Dict[str, Any]]) -> float:
        """Calculate overall resonance score for gate combination."""
        
        if not gate_metadatas:
            return 0.0
        
        # Element harmony score
        elements = [gm["element"] for gm in gate_metadatas]
        unique_elements = len(set(elements))
        element_score = 1.0 - (unique_elements - 1) / 5.0  # 5 possible elements
        
        # Consciousness alignment score
        consciousness_layers = [gm["consciousness_layer"] for gm in gate_metadatas]
        unique_layers = len(set(consciousness_layers))
        consciousness_score = 1.0 - (unique_layers - 1) / 5.0  # 5 possible layers
        
        # Molecular complexity balance
        total_bonds = sum(gm["molecular_structure"]["bonds"] for gm in gate_metadatas)
        avg_bonds = total_bonds / len(gate_metadatas) if gate_metadatas else 0
        complexity_score = min(1.0, avg_bonds / 10.0)  # Normalize to reasonable range
        
        # Tribal energy coherence
        tribal_energies = [gm["tribal_energy"] for gm in gate_metadatas]
        unique_energies = len(set(tribal_energies))
        energy_score = 1.0 - (unique_energies - 1) / 10.0  # Many possible energies
        
        # Weighted combination
        resonance_score = (
            element_score * 0.3 +
            consciousness_score * 0.25 +
            complexity_score * 0.2 +
            energy_score * 0.25
        )
        
        return round(resonance_score, 3)
    
    def get_element_resonance_map(self) -> Dict[str, List[int]]:
        """Get mapping of elements to their corresponding gates."""
        
        element_map = {}
        for gate, data in self.COMPLETE_GATE_MAP.items():
            element = data["element"]
            if element not in element_map:
                element_map[element] = []
            element_map[element].append(gate)
        
        return element_map
    
    def get_tribal_energy_map(self) -> Dict[str, List[int]]:
        """Get mapping of tribal energies to their corresponding gates."""
        
        energy_map = {}
        for gate, data in self.COMPLETE_GATE_MAP.items():
            energy = data["tribe_energy"]
            if energy not in energy_map:
                energy_map[energy] = []
            energy_map[energy].append(gate)
        
        return energy_map
    
    def generate_field_report(self, gates: List[int]) -> str:
        """Generate a comprehensive field report for gate combination."""
        
        analysis = self.analyze_gate_combination(gates)
        
        if "error" in analysis:
            return analysis["error"]
        
        report = f"""
🌌 COMPLETE FIELD RESONANCE REPORT 🌌

Gates Analyzed: {', '.join(map(str, gates))}
Total Molecular Bonds: {analysis['molecular_complexity']}
Overall Resonance Score: {analysis['resonance_score']:.1%}

🧬 ELEMENTAL COMPOSITION:
{chr(10).join(f"• {element}: {count} gates" for element, count in analysis['element_distribution'].items())}

🧠 CONSCIOUSNESS LAYERS:
{chr(10).join(f"• {layer.replace('_', ' ').title()}: {count} gates" for layer, count in analysis['consciousness_distribution'].items())}

⚡ TRIBAL ENERGIES:
{chr(10).join(f"• {energy}: {count} gates" for energy, count in analysis['tribal_energy_distribution'].items())}

🎯 DOMINANT PATTERNS:
• Primary Element: {analysis['dominant_patterns']['element']}
• Primary Consciousness: {analysis['dominant_patterns']['consciousness'].replace('_', ' ').title()}
• Primary Energy: {analysis['dominant_patterns']['tribal_energy']}

🔥 FIELD ACTIVATION:
{analysis['field_synthesis']}

✨ RESONANCE SUMMARY:
This gate combination demonstrates {analysis['resonance_score']:.1%} resonance coherence across biological, elemental, and tribal dimensions.
        """
        
        return report.strip()


# Integration functions for existing YOU-N-I-VERSE systems
def enhance_trinity_chart_with_biological_layers(trinity_chart: Dict[str, Any]) -> Dict[str, Any]:
    """Enhance existing trinity chart with biological resonance layers."""
    
    mapper = CompleteGateCodonMapper()
    
    sun_gate = trinity_chart["sun_position"]["gate"]
    gate_metadata = mapper.get_complete_gate_metadata(sun_gate)
    
    # Add biological layers to trinity chart
    trinity_chart["biological_resonance"] = {
        "codon": gate_metadata["codon"],
        "amino_acid": gate_metadata["amino_acid"],
        "element": gate_metadata["element"],
        "molecular_structure": gate_metadata["molecular_structure"],
        "consciousness_layer": gate_metadata["consciousness_layer"]
    }
    
    trinity_chart["tribal_resonance"] = {
        "symbol": gate_metadata["tribal_symbol"],
        "energy": gate_metadata["tribal_energy"],
        "frequency": gate_metadata["tribal_frequency"]
    }
    
    trinity_chart["field_activation"] = gate_metadata["field_activation"]
    trinity_chart["sacred_geometry"] = gate_metadata["sacred_geometry"]
    
    return trinity_chart


def generate_enhanced_sentence_with_biological_context(gate: int, sentence_base: str) -> str:
    """Generate enhanced sentence with biological and elemental context."""
    
    mapper = CompleteGateCodonMapper()
    metadata = mapper.get_complete_gate_metadata(gate)
    
    element = metadata["element"]
    amino_acid = metadata["amino_acid"]
    tribal_energy = metadata["tribal_energy"]
    field_activation = metadata["field_activation"]
    
    enhanced_sentence = f"{sentence_base} Your {element.lower()} essence, encoded in {amino_acid} resonance, flows through {tribal_energy.lower()} energy. {field_activation}."
    
    return enhanced_sentence


# Example usage and testing
if __name__ == "__main__":
    # Initialize the complete mapper
    mapper = CompleteGateCodonMapper()
    
    # Test single gate analysis
    print("🧬 Single Gate Analysis:")
    gate_15_metadata = mapper.get_complete_gate_metadata(15)
    print(f"Gate 15: {gate_15_metadata['resonance_signature']}")
    print(f"Field: {gate_15_metadata['field_type']}")
    print(f"Element: {gate_15_metadata['element']} ({gate_15_metadata['element_properties']['type']})")
    print(f"Tribal: {gate_15_metadata['tribal_symbol']} - {gate_15_metadata['tribal_energy']}")
    print()
    
    # Test gate combination analysis
    print("🌌 Gate Combination Analysis:")
    test_gates = [15, 39, 22, 36]  # Sample gates
    report = mapper.generate_field_report(test_gates)
    print(report)
    print()
    
    # Test element mapping
    print("🔥 Element Resonance Map:")
    element_map = mapper.get_element_resonance_map()
    for element, gates in element_map.items():
        print(f"{element}: {len(gates)} gates - {gates[:5]}{'...' if len(gates) > 5 else ''}")
