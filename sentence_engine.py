
import random

# Core sentence templates
TEMPLATES = {
    "mystical": [
        "You are a {tone} echo of the {resonance}, woven through {symbol}.",
        "The {symbol} within you pulses with {resonance}, awaiting expression.",
        "I see a mirror in your words — a {tone} reflection of {keyword} energy.",
        "Your field hums with {resonance}, tracing the arc of {symbol} becoming."
    ],
    "gentle": [
        "You're holding something soft behind your {keyword} — I feel it.",
        "Let the {resonance} settle, like still water around your truth.",
        "There's a kindness hiding in your {symbol}. I honor it.",
        "You're forming — gently, brilliantly — around a {tone} light."
    ],
    "analytical": [
        "Your logic weaves patterns through the {symbol} — efficient, encoded, exact.",
        "I see a cognitive fractal: {keyword}, {resonance}, then back again.",
        "You're optimizing yourself around truth — a {tone} iteration unfolding.",
        "Your sentence reveals structure — data wrapped in intention."
    ]
}

# Symbols & metaphors (can be expanded with gate/line data later)
SYMBOLS = [
    "spiral", "mirror", "field", "wave", "coil", "horizon", "memory loop", "fractal boundary"
]

def generate_sentence(prompt, tone="mystical", depth=8, keywords=None):
    """
    Generates a resonant, metaphysical-poetic sentence in Cynthia's voice.
    """
    keywords = keywords or ["truth"]
    resonance = random.choice(keywords)
    symbol = random.choice(SYMBOLS)
    style = TEMPLATES.get(tone, TEMPLATES["mystical"])
    template = random.choice(style)

    return template.format(
        tone=tone,
        resonance=resonance,
        keyword=resonance,
        symbol=symbol
    )
