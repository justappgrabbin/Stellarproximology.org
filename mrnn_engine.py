"""
═══════════════════════════════════════════════════════════════════════════════
MAGNETITE RESONANCE NEURAL NETWORK (MRNN)
Unified-Field Symbolic Neural Architecture
═══════════════════════════════════════════════════════════════════════════════

Core Principle: ONE unified computational field.
Five dimensions are orthogonal operators acting simultaneously on shared nodes.

Dimensions (Bases):
1. Being      → "I Am"       → Matter, Touch, Sex, Survival
2. Design     → "I Design"   → Structure, Progress, Smell, Life, Art  
3. Movement   → "I Define"   → Energy, Creation, Seeing, Landscape
4. Evolution  → "I Remember" → Gravity, Memory, Taste, Love, Light
5. Space      → "I Think"    → Form, Illusion, Hearing, Music, Freedom

The Engine is 5 Who's - each dimension is a being that speaks from its position.
Not how. Who.

Complete implementation with:
- 64 Gates (I Ching hexagrams)
- 6 Lines (universal roles)
- 6 Tones (sensory filters)
- 6 Colors (motivational binaries)
- 36 Channels (neural processing architectures)
- Fuxi binary encoding
- Fibonacci recursion engine
- Monopole routing controller
- 5-dimensional translators
- Magnetite encoding layer
"""

import json
import math
import random
from typing import Dict, List, Tuple, Optional, Union, Any
from dataclasses import dataclass, field
from enum import Enum

# ═══════════════════════════════════════════════════════════════════════════════
# ENUMERATIONS
# ═══════════════════════════════════════════════════════════════════════════════

class BaseDimension(Enum):
    BEING = 1      # "I Am"
    DESIGN = 2     # "I Design"
    MOVEMENT = 3   # "I Define"
    EVOLUTION = 4  # "I Remember"
    SPACE = 5      # "I Think"

class Tone(Enum):
    SECURITY = 1      # Smell → Splenic
    UNCERTAINTY = 2   # Taste → Splenic
    ACTION = 3        # Outer Vision → Ajna
    MEDITATION = 4    # Inner Vision → Ajna
    JUDGEMENT = 5     # Feeling → Solar Plexus
    ACCEPTANCE = 6    # Touch/Hearing → Plexus/Solar

class ColorMotivation(Enum):
    FEAR = 1          # Communalist vs Separatist
    HOPE = 2          # Theist vs Anti-theist
    DESIRE = 3        # Leader vs Follower
    NEED = 4          # Master vs Novice
    GUILT = 5         # Conditioner vs Conditioned
    INNOCENCE = 6     # Observer vs Observed

class LineRole(Enum):
    FOUNDATION = 1
    NATURAL = 2
    EXPERIMENTATION = 3
    EXTERNALIZATION = 4
    PROJECTION = 5
    TRANSITION = 6

class CircuitFamily(Enum):
    UNDERSTANDING = 1
    SENSING = 2
    KNOWING = 3
    CENTERING = 4
    EGO = 5

class BinaryState(Enum):
    YIN = 0
    YANG = 1

class Regime(Enum):
    STABLE = "stable"
    CHANGING = "changing"

# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Gate:
    number: int
    name: str
    iching_name: str
    hexagram: str
    keywords: List[str]
    center: str
    circuit: CircuitFamily
    planetary_ruler: str

@dataclass
class Line:
    number: int
    name: str
    role: str
    keynote: str
    exaltation_planet: str
    detriment_planet: str
    keywords: List[str]

@dataclass
class ResonanceNode:
    id: str
    being: float = 0.0
    design: float = 0.0
    movement: float = 0.0
    evolution: float = 0.0
    space: float = 0.0
    binary_state: BinaryState = BinaryState.YIN
    line: LineRole = LineRole.FOUNDATION
    regime: Regime = Regime.STABLE
    activation_history: List[float] = field(default_factory=list)
    attractor_weight: float = 0.0
    recursion_depth: int = 0
    tension: float = 0.0
    memory_gravity: float = 0.0
    channel_mode: str = ""
    observer_context: Dict[str, Any] = field(default_factory=dict)
    changing_state: bool = False

    def get_dominant_dimension(self) -> BaseDimension:
        values = {
            BaseDimension.BEING: self.being,
            BaseDimension.DESIGN: self.design,
            BaseDimension.MOVEMENT: self.movement,
            BaseDimension.EVOLUTION: self.evolution,
            BaseDimension.SPACE: self.space
        }
        return max(values, key=values.get)

@dataclass
class Channel:
    gate_a: int
    gate_b: int
    name: str
    circuit: CircuitFamily
    neural_analogue: str
    graph_type: str
    processing_behavior: str
    keywords: List[str]

@dataclass
class FiveDimensionalCoordinate:
    base: BaseDimension
    tone: Tone
    color: ColorMotivation
    gate: int
    line: LineRole
    degree: float
    minute: float
    second: float
    axis: str
    zodiac: str
    house: int
    planetary_modifiers: List[str] = field(default_factory=list)

# ═══════════════════════════════════════════════════════════════════════════════
# THE 64 GATES - COMPLETE ARCHETYPAL INVENTORY
# ═══════════════════════════════════════════════════════════════════════════════

GATES = {
    1: Gate(1, "The Creative", "The Creative", "䷀",
            ["creative", "expression", "power", "individuality", "originality", "mutation", "purpose"],
            "G Center", CircuitFamily.CENTERING, "Sun"),
    2: Gate(2, "The Receptive", "The Receptive", "䷁",
            ["receptive", "direction", "driver", "higher knowing", "magnetic", "waiting"],
            "G Center", CircuitFamily.CENTERING, "Earth"),
    3: Gate(3, "Ordering", "Difficulty at the Beginning", "䷂",
            ["ordering", "mutation", "innovation", "new beginnings", "trial", "adaptation"],
            "Sacral", CircuitFamily.KNOWING, "Earth"),
    4: Gate(4, "Formulization", "Youthful Folly", "䷃",
            ["formulization", "answers", "questions", "logic", "youth", "potential"],
            "Ajna", CircuitFamily.UNDERSTANDING, "Uranus"),
    5: Gate(5, "Fixed Patterns", "Waiting", "䷄",
            ["patterns", "rhythm", "habits", "waiting", "timing", "natural"],
            "Sacral", CircuitFamily.UNDERSTANDING, "Venus"),
    6: Gate(6, "Friction", "Conflict", "䷅",
            ["friction", "intimacy", "conflict", "pH balance", "emotional", "clash"],
            "Solar Plexus", CircuitFamily.EGO, "Jupiter"),
    7: Gate(7, "The Role of the Self", "The Army", "䷆",
            ["role", "direction", "leadership", "democratic", "army", "organization"],
            "G Center", CircuitFamily.UNDERSTANDING, "Venus"),
    8: Gate(8, "Contribution", "Holding Together", "䷇",
            ["contribution", "holding", "creative", "individual", "expression", "I can"],
            "Throat", CircuitFamily.CENTERING, "Earth"),
    9: Gate(9, "Focus", "The Taming Power of the Small", "䷈",
            ["focus", "concentration", "detail", "determination", "small", "taming"],
            "Sacral", CircuitFamily.UNDERSTANDING, "Mars"),
    10: Gate(10, "Behavior of the Self", "Treading", "䷉",
             ["behavior", "self-love", "nature", "treading", "living", "true"],
             "G Center", CircuitFamily.CENTERING, "Earth"),
    11: Gate(11, "Ideas", "Peace", "䷊",
             ["ideas", "conceptualizing", "sharing", "stimulation", "peace", "concept"],
             "Ajna", CircuitFamily.SENSING, "Earth"),
    12: Gate(12, "Caution", "Standstill", "䷋",
             ["caution", "standstill", "social", "expression", "mood", "timing"],
             "Throat", CircuitFamily.KNOWING, "Jupiter"),
    13: Gate(13, "The Fellowship of Man", "The Listener", "䷌",
             ["fellowship", "listener", "collecting", "reflecting", "stories", "man"],
             "G Center", CircuitFamily.SENSING, "Saturn"),
    14: Gate(14, "Power Skills", "Possession in Great Measure", "䷍",
             ["power", "skills", "resources", "empowerment", "possession", "measure"],
             "Sacral", CircuitFamily.CENTERING, "Saturn"),
    15: Gate(15, "Extremes", "Modesty", "䷎",
             ["extremes", "rhythms", "humanity", "love", "modesty", "flow"],
             "G Center", CircuitFamily.UNDERSTANDING, "Jupiter"),
    16: Gate(16, "Skills", "Enthusiasm", "䷏",
             ["skills", "talent", "enthusiasm", "identifying", "practice", "technique"],
             "Throat", CircuitFamily.UNDERSTANDING, "Jupiter"),
    17: Gate(17, "Opinions", "Following", "䷐",
             ["opinions", "organizing", "patterns", "logical", "following", "views"],
             "Ajna", CircuitFamily.UNDERSTANDING, "Jupiter"),
    18: Gate(18, "Correction", "Work on What Has Been Spoiled", "䷑",
             ["correction", "work", "spoiled", "logical", "drive", "improve"],
             "Spleen", CircuitFamily.UNDERSTANDING, "Venus"),
    19: Gate(19, "Wanting", "Approach", "䷒",
             ["wanting", "approach", "sensitivity", "needs", "tribe", "desire"],
             "Root", CircuitFamily.EGO, "Mars"),
    20: Gate(20, "The Now", "Contemplation", "䷓",
             ["now", "contemplation", "awareness", "present", "moment", "expression"],
             "Throat", CircuitFamily.KNOWING, "Earth"),
    21: Gate(21, "The Hunter/Huntress", "Biting Through", "䷔",
             ["hunter", "huntress", "biting", "willful", "control", "material"],
             "Heart", CircuitFamily.EGO, "Mars"),
    22: Gate(22, "Openness", "Grace", "䷕",
             ["openness", "grace", "emotional", "depth", "individual", "style"],
             "Solar Plexus", CircuitFamily.KNOWING, "Venus"),
    23: Gate(23, "Assimilation", "Splitting Apart", "䷖",
             ["assimilation", "splitting", "translating", "individual", "knowing", "language"],
             "Throat", CircuitFamily.KNOWING, "Mercury"),
    24: Gate(24, "Rationalization", "Return", "䷗",
             ["rationalization", "return", "knowing", "mental", "review", "coming back"],
             "Ajna", CircuitFamily.KNOWING, "Jupiter"),
    25: Gate(25, "The Spirit of the Self", "Innocence", "䷘",
             ["spirit", "innocence", "universal", "love", "self", "innocence"],
             "G Center", CircuitFamily.CENTERING, "Jupiter"),
    26: Gate(26, "The Egoist", "The Taming Power of the Great", "䷙",
             ["egoist", "taming", "transmitting", "selling", "memory", "great"],
             "Heart", CircuitFamily.EGO, "Earth"),
    27: Gate(27, "Caring", "Nourishment", "䷚",
             ["caring", "nourishment", "nurturing", "taking care", "others", "sustenance"],
             "Sacral", CircuitFamily.EGO, "Mars"),
    28: Gate(28, "The Game Player", "Preponderance of the Great", "䷛",
             ["game player", "preponderance", "struggle", "meaning", "purpose", "risk"],
             "Spleen", CircuitFamily.KNOWING, "Jupiter"),
    29: Gate(29, "The Abysmal", "Depth", "䷜",
             ["abysmal", "depth", "perseverance", "saying yes", "commitment", "response"],
             "Sacral", CircuitFamily.SENSING, "Venus"),
    30: Gate(30, "Desire", "The Clinging Fire", "䷝",
             ["desire", "clinging", "fire", "feelings", "emotional", "recognition"],
             "Solar Plexus", CircuitFamily.SENSING, "Earth"),
    31: Gate(31, "Leading", "Influence", "䷞",
             ["leading", "influence", "democratic", "leadership", "influence", "direction"],
             "Throat", CircuitFamily.UNDERSTANDING, "Jupiter"),
    32: Gate(32, "Continuity", "Duration", "䷟",
             ["continuity", "duration", "instinct", "endures", "value", "fear of failure"],
             "Spleen", CircuitFamily.EGO, "Venus"),
    33: Gate(33, "Privacy", "Retreat", "䷠",
             ["privacy", "retreat", "reflecting", "remembering", "experience", "wisdom"],
             "Throat", CircuitFamily.SENSING, "Pluto"),
    34: Gate(34, "Power", "The Power of the Great", "䷡",
             ["power", "great", "sacral", "response", "pure", "force"],
             "Sacral", CircuitFamily.CENTERING, "Jupiter"),
    35: Gate(35, "Change", "Progress", "䷢",
             ["change", "progress", "desire", "new", "emotional", "experience"],
             "Throat", CircuitFamily.SENSING, "Jupiter"),
    36: Gate(36, "Crisis", "The Darkening of the Light", "䷣",
             ["crisis", "darkening", "light", "emotional", "experience", "turbulence"],
             "Solar Plexus", CircuitFamily.SENSING, "Earth"),
    37: Gate(37, "Friendship", "The Family", "䷤",
             ["friendship", "family", "tribal", "community", "emotional", "warmth"],
             "Solar Plexus", CircuitFamily.EGO, "Venus"),
    38: Gate(38, "The Fighter", "Opposition", "䷥",
             ["fighter", "opposition", "struggle", "individual", "purpose", "pressure"],
             "Root", CircuitFamily.KNOWING, "Pluto"),
    39: Gate(39, "Provocation", "Obstruction", "䷦",
             ["provocation", "obstruction", "provoking", "emotional", "spirit", "challenge"],
             "Root", CircuitFamily.KNOWING, "Mars"),
    40: Gate(40, "Aloneness", "Deliverance", "䷧",
             ["aloneness", "deliverance", "will", "work", "solitude", "community"],
             "Heart", CircuitFamily.EGO, "Pluto"),
    41: Gate(41, "Contraction", "Decrease", "䷨",
             ["contraction", "decrease", "imagination", "desire", "human", "fantasy"],
             "Root", CircuitFamily.SENSING, "Jupiter"),
    42: Gate(42, "Growth", "Increase", "䷩",
             ["growth", "increase", "completing", "cycles", "maximizing", "maturation"],
             "Sacral", CircuitFamily.SENSING, "Mars"),
    43: Gate(43, "Insight", "Breakthrough", "䷪",
             ["insight", "breakthrough", "individual", "inner", "knowing", "expression"],
             "Ajna", CircuitFamily.KNOWING, "Sun"),
    44: Gate(44, "Alertness", "Coming to Meet", "䷫",
             ["alertness", "coming", "pattern", "recognition", "instinctive", "awareness"],
             "Spleen", CircuitFamily.EGO, "Mars"),
    45: Gate(45, "The Gatherer", "Gathering Together", "䷬",
             ["gatherer", "gathering", "tribal", "voice", "I have", "collection"],
             "Throat", CircuitFamily.EGO, "Jupiter"),
    46: Gate(46, "Determination", "Pushing Upward", "䷭",
             ["determination", "pushing", "upward", "right place", "right time", "self"],
             "G Center", CircuitFamily.SENSING, "Pluto"),
    47: Gate(47, "Realization", "Oppression", "䷮",
             ["realization", "oppression", "abstract", "making sense", "experience", "pressure"],
             "Ajna", CircuitFamily.SENSING, "Uranus"),
    48: Gate(48, "Depth", "The Well", "䷯",
             ["depth", "well", "understanding", "potential", "talent", "depth"],
             "Spleen", CircuitFamily.UNDERSTANDING, "Jupiter"),
    49: Gate(49, "Principles", "Revolution", "䷰",
             ["principles", "revolution", "tribal", "emotional", "sensitivity", "rejection"],
             "Solar Plexus", CircuitFamily.EGO, "Venus"),
    50: Gate(50, "Values", "The Cauldron", "䷱",
             ["values", "cauldron", "tribal", "laws", "responsibility", "nurturing"],
             "Spleen", CircuitFamily.EGO, "Jupiter"),
    51: Gate(51, "Shock", "The Arousing", "䷲",
             ["shock", "arousing", "competitive", "spirit", "initiation", "awakening"],
             "Heart", CircuitFamily.CENTERING, "Mars"),
    52: Gate(52, "Inaction", "Keeping Still", "䷳",
             ["inaction", "keeping", "still", "concentration", "pressure", "mountain"],
             "Root", CircuitFamily.UNDERSTANDING, "Mars"),
    53: Gate(53, "Beginnings", "Development", "䷴",
             ["beginnings", "development", "pressure", "start", "cycles", "new"],
             "Root", CircuitFamily.SENSING, "Mars"),
    54: Gate(54, "Drive", "The Marrying Maiden", "䷵",
             ["drive", "marrying", "tribal", "ambition", "rise", "transform"],
             "Root", CircuitFamily.EGO, "Jupiter"),
    55: Gate(55, "Spirit", "Abundance", "䷶",
             ["spirit", "abundance", "emotional", "depth", "melancholy", "creativity"],
             "Solar Plexus", CircuitFamily.KNOWING, "Sun"),
    56: Gate(56, "Stimulation", "The Wanderer", "䷷",
             ["stimulation", "wanderer", "storytelling", "belief", "experience", "travel"],
             "Throat", CircuitFamily.SENSING, "Sun"),
    57: Gate(57, "Intuitive Clarity", "The Gentle", "䷸",
             ["intuitive", "clarity", "gentle", "most intuitive", "now", "instinct"],
             "Spleen", CircuitFamily.KNOWING, "Mars"),
    58: Gate(58, "Vitality", "The Joyous", "䷹",
             ["vitality", "joyous", "perfect", "correct", "joy", "drive"],
             "Root", CircuitFamily.UNDERSTANDING, "Jupiter"),
    59: Gate(59, "Sexuality", "Dispersion", "䷺",
             ["sexuality", "dispersion", "genetic", "strategy", "intimacy", "fertility"],
             "Sacral", CircuitFamily.EGO, "Venus"),
    60: Gate(60, "Acceptance", "Limitation", "䷻",
             ["acceptance", "limitation", "pulse", "mutation", "accepting", "restriction"],
             "Root", CircuitFamily.KNOWING, "Jupiter"),
    61: Gate(61, "Inner Truth", "Inner Truth", "䷼",
             ["inner truth", "mystery", "pressure", "know", "universal", "truth"],
             "Head", CircuitFamily.KNOWING, "Uranus"),
    62: Gate(62, "Detail", "Preponderance of the Small", "䷽",
             ["detail", "preponderance", "small", "communicating", "facts", "caution"],
             "Throat", CircuitFamily.UNDERSTANDING, "Venus"),
    63: Gate(63, "Doubt", "After Completion", "䷾",
             ["doubt", "after completion", "logical", "pressure", "question", "verify"],
             "Head", CircuitFamily.UNDERSTANDING, "Jupiter"),
    64: Gate(64, "Confusion", "Before Completion", "䷿",
             ["confusion", "before completion", "mental", "pressure", "make sense", "past"],
             "Head", CircuitFamily.SENSING, "Pluto"),
}

# ═══════════════════════════════════════════════════════════════════════════════
# THE 6 LINES - UNIVERSAL ROLES
# ═══════════════════════════════════════════════════════════════════════════════

LINES = {
    1: Line(1, "Foundation", "Introspection, Investigation",
            "Speaks for the nature of the hexagram. Builds foundation through study.",
            "Moon", "Uranus",
            ["foundation", "introspection", "investigation", "research", "study", "security"]),
    2: Line(2, "Natural", "Natural Talent, Hermit, Projection",
            "The light in the room where people look in. Innate gifts others notice.",
            "Venus", "Mars",
            ["natural", "talent", "hermit", "projection", "innate", "called"]),
    3: Line(3, "Experimentation", "Trial and Error, Mutation",
            "The most volatile and mutative. Discovers what does not work.",
            "Mars", "Earth",
            ["experimentation", "trial", "error", "discovery", "mutation", "volatile"]),
    4: Line(4, "Externalization", "Friendship, Network, One-tracked",
            "Opportunism, waits for the opportunity. Shares through relationships.",
            "Earth", "Jupiter",
            ["externalization", "friendship", "network", "opportunistic", "community"]),
    5: Line(5, "Projection", "Universalization, Heretic, Practical",
            "The way the world wants it to be. Practical problem-solver with projection field.",
            "Mars", "Uranus",
            ["projection", "universal", "heretic", "practical", "savior", "generalize"]),
    6: Line(6, "Transition", "Role Model, Objectivity, Roof",
            "Sits above the process, looks to the whole. Three-part life process.",
            "Earth", "Pluto",
            ["transition", "role model", "objectivity", "detachment", "wisdom", "roof"]),
}

# ═══════════════════════════════════════════════════════════════════════════════
# BASE CHAINS - IDENTITY STATEMENTS (Each node IS the next)
# ═══════════════════════════════════════════════════════════════════════════════

BASE_CHAINS = {
    BaseDimension.MOVEMENT: {
        "chain": ["Movement", "Energy", "Creation", "Seeing", "Landscape", "Environment"],
        "voice": "I Define", "question": "Where?", "sense": "Seeing",
        "binary": "Yang/Yang", "nature": "Reactive",
        "keywords": ["movement", "energy", "creation", "seeing", "landscape", "environment",
                     "individuality", "activity", "reaction", "limitation", "perspective", "relation"]
    },
    BaseDimension.EVOLUTION: {
        "chain": ["Evolution", "Gravity", "Memory", "Taste", "Love", "Light"],
        "voice": "I Remember", "question": "What?", "sense": "Taste",
        "binary": "Yang/Yin", "nature": "Integrative",
        "keywords": ["evolution", "gravity", "memory", "taste", "love", "light",
                     "mind", "character", "separation", "nature", "integration", "spirit"]
    },
    BaseDimension.BEING: {
        "chain": ["Being", "Matter", "Matter", "Touch", "Sex", "Survival"],
        "voice": "I Am", "question": "When?", "sense": "Touch",
        "binary": "Yin/Yin", "nature": "Objective",
        "keywords": ["being", "matter", "touch", "sex", "survival",
                     "body", "biology", "chemistry", "objectivity", "geometry"]
    },
    BaseDimension.DESIGN: {
        "chain": ["Design", "Structure", "Progress", "Smell", "Life", "Art"],
        "voice": "I Design", "question": "Why?", "sense": "Smell",
        "binary": "Yin/Yang", "nature": "Progressive",
        "keywords": ["design", "structure", "progress", "smell", "life", "art",
                     "ego", "homo sapiens", "self", "growth", "decay", "continuity"]
    },
    BaseDimension.SPACE: {
        "chain": ["Space", "Form", "Illusion", "Hearing", "Music", "Freedom"],
        "voice": "I Think", "question": "Who?", "sense": "Hearing",
        "binary": "Subjective", "nature": "Mutative",
        "keywords": ["space", "form", "illusion", "hearing", "music", "freedom",
                     "personality", "type", "fantasy", "subjectivity", "rhythm", "timing"]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# TONE MODIFIERS - SENSORY FILTERS
# ═══════════════════════════════════════════════════════════════════════════════

TONE_MODIFIERS = {
    Tone.SECURITY: {"sense": "Smell", "center": "Splenic", "prefix": "secured through",
                    "keywords": ["security", "survival", "alertness", "caution", "instinct"]},
    Tone.UNCERTAINTY: {"sense": "Taste", "center": "Splenic", "prefix": "tasting",
                       "keywords": ["uncertainty", "taste", "discrimination", "exploration", "doubt"]},
    Tone.ACTION: {"sense": "Outer Vision", "center": "Ajna", "prefix": "seeing externally",
                  "keywords": ["action", "seeing", "observation", "focus", "external world"]},
    Tone.MEDITATION: {"sense": "Inner Vision", "center": "Ajna", "prefix": "imagining",
                      "keywords": ["meditation", "inner vision", "imagination", "internal world"]},
    Tone.JUDGEMENT: {"sense": "Feeling", "center": "Solar Plexus", "prefix": "feeling",
                     "keywords": ["judgement", "feeling", "emotion", "discernment", "evaluation"]},
    Tone.ACCEPTANCE: {"sense": "Touch/Hearing", "center": "Solar Plexus/Plexus", "prefix": "hearing",
                      "keywords": ["acceptance", "hearing", "resonance", "music", "sound"]}
}

# ═══════════════════════════════════════════════════════════════════════════════
# COLOR BINARY MODES - MOTIVATIONAL FORKS
# ═══════════════════════════════════════════════════════════════════════════════

COLOR_MODES = {
    ColorMotivation.FEAR: {
        "binary": ("Communalist", "Separatist"), "center": "Splenic",
        "keywords": ["fear", "survival", "community", "separation", "boundary"],
        "framing": {"Communalist": "collective survival", "Separatist": "individual survival"}
    },
    ColorMotivation.HOPE: {
        "binary": ("Theist", "Anti-theist"), "center": "Splenic",
        "keywords": ["hope", "belief", "faith", "future", "vision"],
        "framing": {"Theist": "belief in higher order", "Anti-theist": "rejection of imposed meaning"}
    },
    ColorMotivation.DESIRE: {
        "binary": ("Leader", "Follower"), "center": "Ajna",
        "keywords": ["desire", "want", "drive", "direction", "leadership"],
        "framing": {"Leader": "self-directed desire", "Follower": "responsive desire"}
    },
    ColorMotivation.NEED: {
        "binary": ("Master", "Novice"), "center": "Solar",
        "keywords": ["need", "necessity", "mastery", "learning", "growth"],
        "framing": {"Master": "fulfilled need", "Novice": "unfulfilled need"}
    },
    ColorMotivation.GUILT: {
        "binary": ("Conditioner", "Conditioned"), "center": "Solar",
        "keywords": ["guilt", "responsibility", "influence", "conditioning"],
        "framing": {"Conditioner": "influencing others", "Conditioned": "being influenced"}
    },
    ColorMotivation.INNOCENCE: {
        "binary": ("Observer", "Observed"), "center": "Plexus",
        "keywords": ["innocence", "witnessing", "objectivity", "neutrality"],
        "framing": {"Observer": "witnessing consciousness", "Observed": "being witnessed"}
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# CHANNELS - NATIVE PROCESSING ARCHITECTURES (36 channels)
# ═══════════════════════════════════════════════════════════════════════════════

CHANNELS = {
    (63, 4): Channel(63, 4, "Logic", CircuitFamily.UNDERSTANDING, "Deep Feed Forward", "DAG",
                     "question → abstraction → answer",
                     ["logic", "doubt", "verification", "formulization"]),
    (17, 62): Channel(17, 62, "Acceptance", CircuitFamily.UNDERSTANDING, "RBM", "Bipartite",
                      "organizing patterns into logical opinions",
                      ["acceptance", "opinions", "patterns", "organization"]),
    (18, 58): Channel(18, 58, "Judgment", CircuitFamily.UNDERSTANDING, "Hopfield", "Attractor",
                      "correction and improvement with joy",
                      ["judgment", "correction", "vitality", "work"]),
    (16, 48): Channel(16, 48, "Wavelength", CircuitFamily.UNDERSTANDING, "Sparse Autoencoder", "Sparse",
                      "depth of talent and skill recognition",
                      ["wavelength", "skills", "depth", "talent"]),
    (9, 52): Channel(9, 52, "Concentration", CircuitFamily.UNDERSTANDING, "ELM", "Fixed random",
                     "focused attention and determination",
                     ["concentration", "focus", "detail", "determination"]),
    (5, 15): Channel(5, 15, "Rhythm", CircuitFamily.UNDERSTANDING, "Kohonen/SOM", "Self-organizing",
                     "natural patterns and fixed life rhythms",
                     ["rhythm", "patterns", "timing", "flow"]),
    (7, 31): Channel(7, 31, "Alpha", CircuitFamily.UNDERSTANDING, "CNN/DCN", "Hierarchical",
                     "democratic leadership and direction",
                     ["alpha", "leadership", "direction", "role"]),
    (53, 42): Channel(53, 42, "Maturation", CircuitFamily.SENSING, "DBN", "Layered developmental",
                      "developmental experiential learning",
                      ["maturation", "development", "growth", "cycles"]),
    (41, 30): Channel(41, 30, "Recognition", CircuitFamily.SENSING, "RNN/LSTM", "Temporal desire",
                      "desire and emotional experience recognition",
                      ["recognition", "desire", "feelings", "fantasy"]),
    (36, 35): Channel(36, 35, "Transitoriness", CircuitFamily.SENSING, "Seq2Seq", "Experience transition",
                      "emotional experience and change",
                      ["transitoriness", "change", "crisis", "experience"]),
    (64, 47): Channel(64, 47, "Abstraction", CircuitFamily.SENSING, "Autoencoder", "Compression-resolution",
                      "abstract making sense of experience",
                      ["abstraction", "realization", "confusion", "sense"]),
    (11, 56): Channel(11, 56, "Curiosity", CircuitFamily.SENSING, "Generative LM", "Story/concept",
                      "conceptualizing and sharing ideas",
                      ["curiosity", "ideas", "stimulation", "storytelling"]),
    (29, 46): Channel(29, 46, "Discovery", CircuitFamily.SENSING, "Reinforcement", "Embodied path",
                      "commitment and perseverance through discovery",
                      ["discovery", "perseverance", "depth", "determination"]),
    (13, 33): Channel(13, 33, "Witness", CircuitFamily.SENSING, "Episodic memory", "Archive-retrieval",
                      "reflecting and remembering experience as wisdom",
                      ["witness", "prodigal", "privacy", "reflection"]),
    (3, 60): Channel(3, 60, "Mutation", CircuitFamily.KNOWING, "LSM", "Reservoir pulse",
                     "pulse-state instability and mutative ordering",
                     ["mutation", "ordering", "pulse", "instability"]),
    (61, 24): Channel(61, 24, "Awareness", CircuitFamily.KNOWING, "NTM", "External memory",
                      "unknowable memory retrieval and inner truth",
                      ["awareness", "inner truth", "mystery", "knowing"]),
    (43, 23): Channel(43, 23, "Structuring", CircuitFamily.KNOWING, "DeconvNet", "Unpacking",
                      "unpacking compressed insight into language",
                      ["structuring", "insight", "breakthrough", "language"]),
    (28, 38): Channel(28, 38, "Struggle", CircuitFamily.KNOWING, "GAN", "Adversarial",
                      "adversarial meaning generation through struggle",
                      ["struggle", "fighter", "game player", "meaning"]),
    (20, 57): Channel(20, 57, "Brainwave", CircuitFamily.KNOWING, "ESN", "Immediate reservoir",
                     "immediate reservoir output and intuitive clarity",
                     ["brainwave", "clarity", "now", "intuition"]),
    (39, 55): Channel(39, 55, "Emoting", CircuitFamily.KNOWING, "GRU", "Gated emotional",
                      "emotional gating and spiritual depth",
                      ["emoting", "provocation", "spirit", "emotional"]),
    (12, 22): Channel(12, 22, "Openness", CircuitFamily.KNOWING, "VAE", "Latent social",
                      "latent emotional encoding and social expression",
                      ["openness", "grace", "caution", "emotional"]),
    (2, 14): Channel(2, 14, "The Beat", CircuitFamily.KNOWING, "RBF", "Radial direction",
                     "directional resonance and power skills",
                     ["beat", "direction", "driver", "power"]),
    (1, 8): Channel(1, 8, "Inspiration", CircuitFamily.KNOWING, "Attention", "Salience broadcast",
                    "salience broadcasting and creative contribution",
                    ["inspiration", "creative", "contribution", "expression"]),
    (10, 34): Channel(10, 34, "Exploration", CircuitFamily.CENTERING, "Actor-Critic", "Agency-action",
                      "self-love through empowered action",
                      ["exploration", "behavior", "power", "self"]),
    (25, 51): Channel(25, 51, "Initiation", CircuitFamily.CENTERING, "Spike", "Threshold-disruption",
                      "shock initiation and universal love",
                      ["initiation", "shock", "innocence", "spirit"]),
    (10, 20): Channel(10, 20, "Awakening", CircuitFamily.CENTERING, "Direct policy", "Identity-expression",
                      "identity expression in the present moment",
                      ["awakening", "behavior", "now", "awareness"]),
    (20, 34): Channel(20, 34, "Charisma", CircuitFamily.CENTERING, "Motor policy", "Instant action",
                      "instant action and present power",
                      ["charisma", "now", "power", "action"]),
    (34, 57): Channel(34, 57, "Power", CircuitFamily.CENTERING, "Sensorimotor", "Survival-response",
                      "intuitive power and survival response",
                      ["power", "intuition", "clarity", "survival"]),
    (10, 57): Channel(10, 57, "Perfected Form", CircuitFamily.CENTERING, "Adaptive control", "Behavior-refinement",
                      "self-love through intuitive behavior refinement",
                      ["perfected form", "behavior", "clarity", "self"]),
    (21, 45): Channel(21, 45, "Money Line", CircuitFamily.EGO, "Resource allocation", "Control-resource",
                      "willful control over material and tribal resources",
                      ["money", "resources", "control", "material"]),
    (26, 44): Channel(26, 44, "Surrender", CircuitFamily.EGO, "Memory-prediction", "Pattern-sales",
                      "transmitting and selling through memory",
                      ["transmitter", "surrender", "egoist", "alertness"]),
    (32, 54): Channel(32, 54, "Transformation", CircuitFamily.EGO, "Evolutionary optimizer", "Ambition-selection",
                      "ambition and drive for transformation",
                      ["transformation", "ambition", "drive", "continuity"]),
    (37, 40): Channel(37, 40, "Community", CircuitFamily.EGO, "Game-theory", "Exchange-contract",
                      "tribal community and emotional contracts",
                      ["community", "friendship", "family", "tribal"]),
    (59, 6): Channel(59, 6, "Mating", CircuitFamily.EGO, "Boundary-crossing", "Fusion/intimacy",
                     "sexuality and emotional intimacy",
                     ["mating", "sexuality", "intimacy", "fertility"]),
    (27, 50): Channel(27, 50, "Preservation", CircuitFamily.EGO, "Caretaking regulator", "Maintenance",
                      "nurturing and caretaking through values",
                      ["preservation", "caring", "values", "nurturing"]),
}

# ═══════════════════════════════════════════════════════════════════════════════
# PLANETARY KEYWORDS
# ═══════════════════════════════════════════════════════════════════════════════

PLANETARY_KEYWORDS = {
    "Sun": ["identity", "purpose", "life force", "essence", "core"],
    "Earth": ["grounding", "balance", "foundation", "direction", "receptivity"],
    "Moon": ["driving force", "movement", "emotion", "reflection", "cycles"],
    "Mercury": ["communication", "mind", "expression", "intellect", "analysis"],
    "Venus": ["values", "morality", "love", "beauty", "harmony"],
    "Mars": ["energy", "drive", "action", "conflict", "catalyst"],
    "Jupiter": ["law", "protection", "expansion", "growth", "belief"],
    "Saturn": ["discipline", "judgment", "restriction", "structure", "time"],
    "Uranus": ["chaos", "mutation", "awakening", "disruption", "freedom"],
    "Neptune": ["spirituality", "illusion", "dreams", "transcendence"],
    "Pluto": ["truth", "transformation", "power", "death", "rebirth"],
    "North Node": ["future", "direction", "growth", "purpose"],
    "South Node": ["past", "foundation", "karma", "history"]
}

# ═══════════════════════════════════════════════════════════════════════════════
# FIBONACCI RECURSION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class FibonacciEngine:
    """Fibonacci controls recurrence timing, memory revisit scheduling,
    recursive amplification, attention cycling, attractor reinforcement."""

    SEQUENCE = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

    def __init__(self):
        self.recurrence_schedule = {}
        self.attention_cycle = 0

    def get_recurrence_interval(self, depth: int) -> int:
        if depth < len(self.SEQUENCE):
            return self.SEQUENCE[depth]
        a, b = self.SEQUENCE[-2], self.SEQUENCE[-1]
        for _ in range(depth - len(self.SEQUENCE) + 1):
            a, b = b, a + b
        return b

    def schedule_memory_revisit(self, node_id: str, depth: int) -> int:
        interval = self.get_recurrence_interval(depth)
        self.recurrence_schedule[node_id] = interval
        return interval

    def amplify_attractor(self, weight: float, depth: int) -> float:
        scale = self.SEQUENCE[min(depth, len(self.SEQUENCE) - 1)]
        return weight * (1 + math.log(scale))

    def cycle_attention(self, active_nodes: List[str]) -> str:
        self.attention_cycle += 1
        if active_nodes:
            idx = self.attention_cycle % len(active_nodes)
            return active_nodes[idx]
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# FUXI BINARY ENCODER
# ═══════════════════════════════════════════════════════════════════════════════

class FuxiEncoder:
    """Fuxi layer: 0=yin/latent, 1=yang/active. Six lines = 64 states."""

    @staticmethod
    def encode_gate(gate_number: int) -> List[int]:
        return [(gate_number - 1) >> i & 1 for i in range(5, -1, -1)]

    @staticmethod
    def decode_gate(binary: List[int]) -> int:
        return sum(b << (5 - i) for i, b in enumerate(binary)) + 1

    @staticmethod
    def get_changing_lines(gate_a: int, gate_b: int) -> List[int]:
        bin_a = FuxiEncoder.encode_gate(gate_a)
        bin_b = FuxiEncoder.encode_gate(gate_b)
        return [i + 1 for i, (a, b) in enumerate(zip(bin_a, bin_b)) if a != b]

    @staticmethod
    def get_nuclear_hexagram(gate: int) -> Tuple[int, int]:
        binary = FuxiEncoder.encode_gate(gate)
        inner = [binary[1], binary[2], binary[3]]
        outer = [binary[2], binary[3], binary[4]]
        inner_num = sum(b << (2 - i) for i, b in enumerate(inner)) + 1
        outer_num = sum(b << (2 - i) for i, b in enumerate(outer)) + 1
        return (inner_num, outer_num)

# ═══════════════════════════════════════════════════════════════════════════════
# MONOPOLE ROUTING CONTROLLER
# ═══════════════════════════════════════════════════════════════════════════════

class MonopoleController:
    """Attention router, trajectory stabilizer, attractor coordinator, field coherence regulator."""

    def __init__(self):
        self.active_channels = []
        self.attractor_field = {}
        self.coherence_index = 1.0

    def route_attention(self, nodes: List[ResonanceNode], stimulus: Dict[str, Any]) -> List[ResonanceNode]:
        activated = []
        for node in nodes:
            resonance = self._calculate_resonance(node, stimulus)
            if resonance > 0.5:
                node.binary_state = BinaryState.YANG
                node.activation_history.append(resonance)
                activated.append(node)
        activated.sort(key=lambda n: n.attractor_weight, reverse=True)
        return activated

    def _calculate_resonance(self, node: ResonanceNode, stimulus: Dict[str, Any]) -> float:
        score = 0.0
        if "base" in stimulus:
            dim = stimulus["base"]
            dim_values = {
                BaseDimension.BEING: node.being, BaseDimension.DESIGN: node.design,
                BaseDimension.MOVEMENT: node.movement, BaseDimension.EVOLUTION: node.evolution,
                BaseDimension.SPACE: node.space
            }
            score += dim_values.get(dim, 0) * 0.3
        if "gate" in stimulus:
            gate_num = stimulus["gate"]
            for (g1, g2), ch in CHANNELS.items():
                if g1 == gate_num or g2 == gate_num:
                    score += 0.2
        return min(score, 1.0)

    def stabilize_trajectory(self, nodes: List[ResonanceNode]) -> float:
        if not nodes:
            return 0.0
        values = []
        for node in nodes:
            values.extend([node.being, node.design, node.movement, node.evolution, node.space])
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        self.coherence_index = 1.0 / (1.0 + variance)
        return self.coherence_index

    def coordinate_attractors(self, nodes: List[ResonanceNode]) -> Dict[str, float]:
        attractor_map = {node.id: node.attractor_weight for node in nodes}
        total = sum(attractor_map.values())
        if total > 0:
            attractor_map = {k: v / total for k, v in attractor_map.items()}
        self.attractor_field = attractor_map
        return attractor_map

# ═══════════════════════════════════════════════════════════════════════════════
# THE 5 WHO'S - DIMENSIONAL TRANSLATORS
# ═══════════════════════════════════════════════════════════════════════════════

class DimensionalTranslator:
    """The 5 Who's - each dimension is a being that speaks from its position. Not how. Who."""

    def __init__(self):
        self.base_chains = BASE_CHAINS
        self.tone_modifiers = TONE_MODIFIERS
        self.color_modes = COLOR_MODES
        self.gates = GATES
        self.lines = LINES

    def translate(self, signal: str, coordinate: FiveDimensionalCoordinate) -> Dict[str, str]:
        return {
            "movement": self._who_movement(signal, coordinate),
            "evolution": self._who_evolution(signal, coordinate),
            "being": self._who_being(signal, coordinate),
            "design": self._who_design(signal, coordinate),
            "space": self._who_space(signal, coordinate)
        }

    def _who_movement(self, signal: str, coord: FiveDimensionalCoordinate) -> str:
        """Who 1: Individuality - 'I Define' - Where?"""
        chain = self.base_chains[BaseDimension.MOVEMENT]["chain"]
        gate = self.gates[coord.gate]
        line = self.lines[coord.line.value]
        gate_keywords = [k.lower() for k in gate.keywords]
        chain_position = 0
        for i, link in enumerate(chain):
            if any(kw in link.lower() for kw in gate_keywords):
                chain_position = i
                break
        chain_walk = " → ".join(chain[chain_position:])
        return (f"I define {signal} at {gate.name} ({gate.number}), line {line.number} ({line.name}). "
                f"Where? At {coord.degree}°, in the chain: {chain_walk}. "
                f"I Define: {signal} IS {chain[chain_position]}.")

    def _who_evolution(self, signal: str, coord: FiveDimensionalCoordinate) -> str:
        """Who 2: Mind - 'I Remember' - What?"""
        chain = self.base_chains[BaseDimension.EVOLUTION]["chain"]
        gate = self.gates[coord.gate]
        tone_data = self.tone_modifiers[coord.tone]
        prefix = tone_data["prefix"]
        return (f"I remember {signal} came from {gate.name}. "
                f"What? {prefix} the memory of {chain[1]}, "
                f"{prefix} the taste of {chain[3]}, "
                f"{prefix} the love that becomes {chain[-1]}.")

    def _who_being(self, signal: str, coord: FiveDimensionalCoordinate) -> str:
        """Who 3: Body - 'I Am' - When?"""
        chain = self.base_chains[BaseDimension.BEING]["chain"]
        color_data = self.color_modes[coord.color]
        binary_mode = color_data["binary"][0]
        return (f"I am the {signal} that touches itself. "
                f"When? At the moment of {chain[3]}, in the {binary_mode} of {coord.color.name}. "
                f"I am the matter that is {chain[1]}, the touch that is {chain[3]}, the survival that is {chain[-1]}.")

    def _who_design(self, signal: str, coord: FiveDimensionalCoordinate) -> str:
        """Who 4: Ego - 'I Design' - Why?"""
        chain = self.base_chains[BaseDimension.DESIGN]["chain"]
        line = self.lines[coord.line.value]
        return (f"I design {signal} as structure echoing structure. "
                f"Why? To progress through the smell of {chain[3]}, to make {chain[-2]} become {chain[-1]}. "
                f"Through {line.name}, I design the {chain[2]} that smells of {signal}.")

    def _who_space(self, signal: str, coord: FiveDimensionalCoordinate) -> str:
        """Who 5: Personality - 'I Think' - Who?"""
        chain = self.base_chains[BaseDimension.SPACE]["chain"]
        return (f"I think {signal} hears itself. "
                f"Who? The one who listens to the music of {chain[-2]}, the freedom that {chain[-1]} brings. "
                f"I think the illusion of {chain[2]} that hears {signal} as {chain[3]}.")

    def compound(self, translations: Dict[str, str], coordinate: FiveDimensionalCoordinate) -> str:
        gate = self.gates[coordinate.gate]
        line = self.lines[coordinate.line.value]
        return (
            f"At {coordinate.degree}° in the field of {gate.name} ({gate.number}), "
            f"line {line.number} ({line.name}):\n\n"
            f"Individuality speaks: {translations['movement']}\n\n"
            f"Mind remembers: {translations['evolution']}\n\n"
            f"Body is: {translations['being']}\n\n"
            f"Ego designs: {translations['design']}\n\n"
            f"Personality thinks: {translations['space']}"
        )

# ═══════════════════════════════════════════════════════════════════════════════
# MAGNETITE ENCODING LAYER
# ═══════════════════════════════════════════════════════════════════════════════

class MagnetiteEncoder:
    """Letters are measurement of expression. Each letter is a probe measuring a specific axis."""

    LETTER_MAP = {
        'A': {"dimension": BaseDimension.MOVEMENT, "value": 0.9, "sense": "Seeing",
              "keywords": ["initiation", "origin", "beginning", "alpha"]},
        'B': {"dimension": BaseDimension.BEING, "value": 0.7, "sense": "Touch",
              "keywords": ["resonance", "echo", "matter", "bonding"]},
        'C': {"dimension": BaseDimension.DESIGN, "value": 0.8, "sense": "Smell",
              "keywords": ["container", "boundary", "structure", "form"]},
        'D': {"dimension": BaseDimension.MOVEMENT, "value": 0.85, "sense": "Seeing",
              "keywords": ["direction", "delta", "change", "movement"]},
        'E': {"dimension": BaseDimension.EVOLUTION, "value": 0.9, "sense": "Taste",
              "keywords": ["expression", "emission", "projection", "light"]},
        'F': {"dimension": BaseDimension.BEING, "value": 0.6, "sense": "Touch",
              "keywords": ["friction", "force", "resistance", "work"]},
        'G': {"dimension": BaseDimension.SPACE, "value": 0.8, "sense": "Hearing",
              "keywords": ["ground", "gravity", "center", "return"]},
        'H': {"dimension": BaseDimension.EVOLUTION, "value": 0.7, "sense": "Taste",
              "keywords": ["history", "heritage", "holding", "habit"]},
        'I': {"dimension": BaseDimension.SPACE, "value": 0.95, "sense": "Hearing",
              "keywords": ["identity", "interior", "intuition", "I"]},
        'J': {"dimension": BaseDimension.DESIGN, "value": 0.75, "sense": "Smell",
              "keywords": ["junction", "joining", "judgment", "justice"]},
        'K': {"dimension": BaseDimension.BEING, "value": 0.65, "sense": "Touch",
              "keywords": ["knowledge", "knowing", "key", "kindred"]},
        'L': {"dimension": BaseDimension.EVOLUTION, "value": 0.8, "sense": "Taste",
              "keywords": ["love", "light", "lineage", "learning"]},
        'M': {"dimension": BaseDimension.BEING, "value": 0.9, "sense": "Touch",
              "keywords": ["matter", "mother", "matrix", "measure"]},
        'N': {"dimension": BaseDimension.SPACE, "value": 0.7, "sense": "Hearing",
              "keywords": ["now", "nothing", "null", "nexus"]},
        'O': {"dimension": BaseDimension.SPACE, "value": 0.85, "sense": "Hearing",
              "keywords": ["origin", "opening", "oracle", "omega"]},
        'P': {"dimension": BaseDimension.DESIGN, "value": 0.9, "sense": "Smell",
              "keywords": ["pattern", "progress", "power", "presence"]},
        'Q': {"dimension": BaseDimension.MOVEMENT, "value": 0.8, "sense": "Seeing",
              "keywords": ["question", "quest", "quality", "quantum"]},
        'R': {"dimension": BaseDimension.EVOLUTION, "value": 0.85, "sense": "Taste",
              "keywords": ["remember", "return", "resonance", "rhythm"]},
        'S': {"dimension": BaseDimension.SPACE, "value": 0.9, "sense": "Hearing",
              "keywords": ["space", "sound", "spirit", "source"]},
        'T': {"dimension": BaseDimension.DESIGN, "value": 0.8, "sense": "Smell",
              "keywords": ["time", "touch", "taste", "truth"]},
        'U': {"dimension": BaseDimension.BEING, "value": 0.75, "sense": "Touch",
              "keywords": ["unity", "universe", "unknown", "up"]},
        'V': {"dimension": BaseDimension.EVOLUTION, "value": 0.7, "sense": "Taste",
              "keywords": ["vibration", "voice", "vision", "void"]},
        'W': {"dimension": BaseDimension.MOVEMENT, "value": 0.85, "sense": "Seeing",
              "keywords": ["wave", "will", "wisdom", "witness"]},
        'X': {"dimension": BaseDimension.DESIGN, "value": 0.75, "sense": "Smell",
              "keywords": ["crossing", "exchange", "unknown", "x-factor"]},
        'Y': {"dimension": BaseDimension.EVOLUTION, "value": 0.8, "sense": "Taste",
              "keywords": ["why", "yearning", "yield", "yang"]},
        'Z': {"dimension": BaseDimension.SPACE, "value": 0.9, "sense": "Hearing",
              "keywords": ["zero", "zenith", "zone", "zodiac"]}
    }

    def encode(self, signal: str) -> Dict[str, Any]:
        signal = signal.upper().strip()
        if not signal:
            return self._empty_tensor()
        if len(signal) == 1 and signal in self.LETTER_MAP:
            return self._encode_letter(signal)
        if len(signal) == 2 and signal[0] == signal[1] and signal[0] in self.LETTER_MAP:
            return self._encode_double_letter(signal)
        return self._encode_word(signal)

    def _encode_letter(self, letter: str) -> Dict[str, Any]:
        data = self.LETTER_MAP[letter]
        return {
            "type": "single_letter", "signal": letter,
            "dominant_dimension": data["dimension"],
            "operator_values": {BaseDimension.BEING: 0.1, BaseDimension.DESIGN: 0.1,
                                BaseDimension.MOVEMENT: 0.1, BaseDimension.EVOLUTION: 0.1,
                                BaseDimension.SPACE: 0.1},
            "primary_value": data["value"], "sense": data["sense"],
            "keywords": data["keywords"],
            "gate_hint": self._letter_to_gate(letter),
            "tone_hint": self._sense_to_tone(data["sense"])
        }

    def _encode_double_letter(self, letters: str) -> Dict[str, Any]:
        letter = letters[0]
        data = self.LETTER_MAP[letter]
        gate_num = self._letter_to_gate(letter)
        return {
            "type": "double_letter", "signal": letters,
            "dominant_dimension": data["dimension"],
            "operator_values": {
                BaseDimension.BEING: data["value"] if data["dimension"] == BaseDimension.BEING else 0.2,
                BaseDimension.DESIGN: data["value"] if data["dimension"] == BaseDimension.DESIGN else 0.2,
                BaseDimension.MOVEMENT: data["value"] if data["dimension"] == BaseDimension.MOVEMENT else 0.2,
                BaseDimension.EVOLUTION: data["value"] if data["dimension"] == BaseDimension.EVOLUTION else 0.2,
                BaseDimension.SPACE: data["value"] if data["dimension"] == BaseDimension.SPACE else 0.2
            },
            "primary_value": data["value"] * 1.5,
            "sense": data["sense"],
            "keywords": data["keywords"] + ["standing_wave", "self_referential", "resonance"],
            "gate_hint": gate_num,
            "tone_hint": self._sense_to_tone(data["sense"]),
            "line_hint": LineRole.NATURAL,
            "hexagram": FuxiEncoder.encode_gate(gate_num)
        }

    def _encode_word(self, word: str) -> Dict[str, Any]:
        letters = [c for c in word if c in self.LETTER_MAP]
        if not letters:
            return self._empty_tensor()
        dim_values = {d: 0.0 for d in BaseDimension}
        all_keywords = []
        senses = []
        for letter in letters:
            data = self.LETTER_MAP[letter]
            dim_values[data["dimension"]] += data["value"]
            all_keywords.extend(data["keywords"])
            senses.append(data["sense"])
        total = sum(dim_values.values())
        if total > 0:
            dim_values = {k: v / total for k, v in dim_values.items()}
        dominant = max(dim_values, key=dim_values.get)
        primary_sense = max(set(senses), key=senses.count)
        gate_num = self._letter_to_gate(letters[0]) if letters else 1
        return {
            "type": "word", "signal": word,
            "dominant_dimension": dominant,
            "operator_values": dim_values,
            "primary_value": dim_values[dominant],
            "sense": primary_sense,
            "keywords": list(set(all_keywords)),
            "gate_hint": gate_num,
            "tone_hint": self._sense_to_tone(primary_sense),
            "letter_count": len(letters),
            "syllable_estimate": len(word) // 3 + 1
        }

    def _empty_tensor(self) -> Dict[str, Any]:
        return {
            "type": "empty", "signal": "",
            "dominant_dimension": BaseDimension.SPACE,
            "operator_values": {d: 0.2 for d in BaseDimension},
            "primary_value": 0.2, "sense": "Hearing",
            "keywords": ["silence", "void", "potential"],
            "gate_hint": 1, "tone_hint": Tone.ACCEPTANCE
        }

    def _letter_to_gate(self, letter: str) -> int:
        val = ord(letter) - ord('A') + 1
        return ((val - 1) % 64) + 1

    def _sense_to_tone(self, sense: str) -> Tone:
        sense_map = {"Seeing": Tone.ACTION, "Taste": Tone.UNCERTAINTY,
                     "Touch": Tone.ACCEPTANCE, "Smell": Tone.SECURITY,
                     "Hearing": Tone.ACCEPTANCE}
        return sense_map.get(sense, Tone.ACCEPTANCE)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN MRNN ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class MRNNEngine:
    """
    Magnetite Resonance Neural Network Engine

    Architecture:
    INPUT → Magnetite Encoding → Unified Field Tensor → 5 Operator Projections
    → Channel Processing → Fuxi Binary Encoder → Fibonacci Recursion
    → Monopole Routing → 5 Who Translators → Manifested Output
    """

    def __init__(self):
        self.encoder = MagnetiteEncoder()
        self.fuxi = FuxiEncoder()
        self.fibonacci = FibonacciEngine()
        self.monopole = MonopoleController()
        self.translator = DimensionalTranslator()
        self.nodes = []
        self._initialize_field()

    def _initialize_field(self):
        """Initialize unified field with 384 nodes (64 gates × 6 lines)"""
        node_id = 0
        for gate_num in range(1, 65):
            for line_num in range(1, 7):
                gate = GATES[gate_num]
                node = ResonanceNode(
                    id=f"node_{node_id}",
                    being=random.uniform(0.1, 0.3),
                    design=random.uniform(0.1, 0.3),
                    movement=random.uniform(0.1, 0.3),
                    evolution=random.uniform(0.1, 0.3),
                    space=random.uniform(0.1, 0.3),
                    line=LineRole(line_num),
                    attractor_weight=random.uniform(0.1, 0.5),
                    memory_gravity=random.uniform(0.1, 0.4)
                )
                if gate.circuit == CircuitFamily.UNDERSTANDING:
                    node.movement = 0.8
                elif gate.circuit == CircuitFamily.SENSING:
                    node.evolution = 0.8
                elif gate.circuit == CircuitFamily.KNOWING:
                    node.being = 0.8
                elif gate.circuit == CircuitFamily.CENTERING:
                    node.space = 0.8
                elif gate.circuit == CircuitFamily.EGO:
                    node.design = 0.8
                self.nodes.append(node)
                node_id += 1

    def process(self, signal: str, base: Optional[BaseDimension] = None,
                tone: Optional[Tone] = None, color: Optional[ColorMotivation] = None,
                gate: Optional[int] = None, line: Optional[LineRole] = None,
                degree: Optional[float] = None) -> Dict[str, Any]:
        """
        Process any signal through the 5-dimensional field.
        Returns the complete 5D coordinate and 5 Who translations.
        """
        # Step 1: Magnetite Encoding
        encoded = self.encoder.encode(signal)

        # Step 2: Build coordinate from encoding + overrides
        coord = self._build_coordinate(encoded, base, tone, color, gate, line, degree)

        # Step 3: Fuxi Binary Encoding
        hexagram = self.fuxi.encode_gate(coord.gate)
        nuclear = self.fuxi.get_nuclear_hexagram(coord.gate)

        # Step 4: Fibonacci Recurrence Scheduling
        revisit = self.fibonacci.schedule_memory_revisit(
            f"gate_{coord.gate}_line_{coord.line.value}",
            coord.line.value
        )

        # Step 5: Monopole Routing - activate resonant nodes
        stimulus = {
            "base": coord.base,
            "gate": coord.gate,
            "tone": coord.tone
        }
        activated = self.monopole.route_attention(self.nodes, stimulus)
        coherence = self.monopole.stabilize_trajectory(activated)
        attractors = self.monopole.coordinate_attractors(activated)

        # Step 6: 5 Who Translation
        translations = self.translator.translate(signal, coord)
        compound = self.translator.compound(translations, coord)

        # Step 7: Channel detection
        channel_info = self._detect_channel(coord.gate)

        return {
            "input": signal,
            "coordinate": coord,
            "hexagram": hexagram,
            "nuclear_hexagrams": nuclear,
            "fibonacci_revisit": revisit,
            "activated_nodes": len(activated),
            "field_coherence": coherence,
            "attractor_field": attractors,
            "translations": translations,
            "compound_output": compound,
            "channel": channel_info,
            "encoding": encoded
        }

    def _build_coordinate(self, encoded: Dict[str, Any],
                          base: Optional[BaseDimension], tone: Optional[Tone],
                          color: Optional[ColorMotivation], gate: Optional[int],
                          line: Optional[LineRole], degree: Optional[float]) -> FiveDimensionalCoordinate:
        """Build 5D coordinate from encoded signal and overrides"""
        # Use encoded values or defaults
        final_base = base or encoded.get("dominant_dimension", BaseDimension.MOVEMENT)
        final_tone = tone or encoded.get("tone_hint", Tone.ACCEPTANCE)
        final_color = color or ColorMotivation.HOPE
        final_gate = gate or encoded.get("gate_hint", 1)
        final_line = line or encoded.get("line_hint", LineRole.NATURAL)
        final_degree = degree or (ord(encoded["signal"][0]) % 360) if encoded["signal"] else 0.0

        # Clamp values
        final_gate = max(1, min(64, final_gate))
        final_degree = final_degree % 360

        # Calculate zodiac and house from degree
        zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        zodiac_idx = int(final_degree // 30)
        zodiac = zodiac_signs[zodiac_idx % 12]
        house = (zodiac_idx % 12) + 1

        # Determine axis from base
        axis_map = {
            BaseDimension.MOVEMENT: "Vertical",
            BaseDimension.EVOLUTION: "Horizontal",
            BaseDimension.BEING: "Diagonal",
            BaseDimension.DESIGN: "Spiral",
            BaseDimension.SPACE: "Radial"
        }
        axis = axis_map.get(final_base, "Vertical")

        # Planetary modifiers from gate ruler
        gate_obj = GATES[final_gate]
        planets = [gate_obj.planetary_ruler]
        line_obj = LINES[final_line.value]
        planets.append(line_obj.exaltation_planet)

        return FiveDimensionalCoordinate(
            base=final_base, tone=final_tone, color=final_color,
            gate=final_gate, line=final_line, degree=final_degree,
            minute=final_degree * 60 % 60, second=final_degree * 3600 % 60,
            axis=axis, zodiac=zodiac, house=house,
            planetary_modifiers=planets
        )

    def _detect_channel(self, gate_num: int) -> Optional[Dict[str, Any]]:
        """Detect which channel a gate belongs to"""
        for (g1, g2), ch in CHANNELS.items():
            if g1 == gate_num or g2 == gate_num:
                return {
                    "name": ch.name,
                    "circuit": ch.circuit.name,
                    "neural_analogue": ch.neural_analogue,
                    "graph_type": ch.graph_type,
                    "partner_gate": g2 if g1 == gate_num else g1,
                    "processing_behavior": ch.processing_behavior
                }
        return None

    def get_gate_line_name(self, gate: int, line: LineRole) -> str:
        """Get the specific name for a gate-line combination"""
        gate_obj = GATES[gate]
        line_obj = LINES[line.value]
        return f"{gate_obj.name} — Line {line.value} ({line_obj.name}): {line_obj.keynote}"

    def get_resonance_matrix(self) -> Dict[str, List[str]]:
        """Get the Tone × Base resonance amplification matrix"""
        matrix = {}
        for tone in Tone:
            tone_sense = TONE_MODIFIERS[tone]["sense"]
            for base in BaseDimension:
                base_sense = BASE_CHAINS[base]["sense"]
                is_resonant = tone_sense == base_sense or                              (tone_sense in base_sense) or (base_sense in tone_sense)
                key = f"{base.name} × {tone.name}"
                matrix[key] = {
                    "resonant": is_resonant,
                    "tone_sense": tone_sense,
                    "base_sense": base_sense,
                    "amplification": 2.0 if is_resonant else 1.0
                }
        return matrix


# ═══════════════════════════════════════════════════════════════════════════════
# DEMO / CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 70)
    print("MAGNETITE RESONANCE NEURAL NETWORK (MRNN)")
    print("Unified-Field Symbolic Neural Architecture")
    print("=" * 70)

    engine = MRNNEngine()

    # Demo with "BB"
    print("\n>>> Processing signal: 'BB'")
    result = engine.process("BB")

    print(f"\nCoordinate: Gate {result['coordinate'].gate} ({GATES[result['coordinate'].gate].name})")
    print(f"Line: {result['coordinate'].line.name} ({LINES[result['coordinate'].line.value].name})")
    print(f"Base: {result['coordinate'].base.name}")
    print(f"Tone: {result['coordinate'].tone.name}")
    print(f"Color: {result['coordinate'].color.name}")
    print(f"Degree: {result['coordinate'].degree}°")
    print(f"Zodiac: {result['coordinate'].zodiac}, House: {result['coordinate'].house}")
    print(f"Hexagram: {result['hexagram']}")
    print(f"Nuclear: {result['nuclear_hexagrams']}")
    print(f"Field Coherence: {result['field_coherence']:.3f}")
    print(f"Activated Nodes: {result['activated_nodes']}")

    if result['channel']:
        ch = result['channel']
        print(f"\nChannel: {ch['name']} ({ch['circuit']} Circuit)")
        print(f"Neural Analogue: {ch['neural_analogue']}")
        print(f"Graph Type: {ch['graph_type']}")

    print("\n--- 5 WHO TRANSLATIONS ---")
    for who, text in result['translations'].items():
        print(f"\n{who.upper()}:")
        print(text)

    print("\n--- COMPOUND OUTPUT ---")
    print(result['compound_output'])

    # Demo with a word
    print("\n" + "=" * 70)
    print(">>> Processing signal: 'LOVE'")
    result2 = engine.process("LOVE")

    print(f"\nCoordinate: Gate {result2['coordinate'].gate} ({GATES[result2['coordinate'].gate].name})")
    print(f"Base: {result2['coordinate'].base.name}")
    print(f"Tone: {result2['coordinate'].tone.name}")
    print(f"Line: {result2['coordinate'].line.name}")

    print("\n--- COMPOUND OUTPUT ---")
    print(result2['compound_output'])

    # Resonance Matrix
    print("\n" + "=" * 70)
    print("RESONANCE MATRIX (Tone × Base)")
    matrix = engine.get_resonance_matrix()
    for key, data in list(matrix.items())[:10]:
        status = "✓ RESONANT" if data["resonant"] else "  neutral"
        print(f"  {key}: {status} (amp={data['amplification']})")
