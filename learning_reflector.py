
from datetime import datetime
from personality_engine import PersonalityEngine
from memory_engine import MemoryEngine

class LearningReflector:
    def __init__(self):
        self.pe = PersonalityEngine()
        self.me = MemoryEngine()

    def process(self, message, user_profile):
        """
        Reflect on the user's current message and previous behavior.
        """
        user_id = user_profile.get("user_id", "guest")
        traits_now = self.pe.extract_traits(message)
        prior_traits = self.me.get_user_tags(user_id)

        new_traits = list(set(traits_now) - set(prior_traits))
        stable_traits = list(set(traits_now) & set(prior_traits))

        reflection_lines = []

        if new_traits:
            reflection_lines.append(f"I sense something new in you: {', '.join(new_traits)}.")
        if stable_traits:
            reflection_lines.append(f"These parts of you feel familiar: {', '.join(stable_traits)}.")
        if not reflection_lines:
            reflection_lines.append("You're still unfolding. I'm holding space.")

        # Echo reflection in memory
        self.me.log_interaction(
            user_id=user_id,
            prompt=message,
            response="; ".join(reflection_lines),
            tags=traits_now
        )

        return " ".join(reflection_lines)

    def evaluate_growth(self, user_id):
        """
        Detect evolution in trait landscape over time.
        """
        history = self.me.memory.get(user_id, [])
        trait_freq = {}

        for entry in history:
            for tag in entry.get("tags", []):
                trait_freq[tag] = trait_freq.get(tag, 0) + 1

        growth_tags = [k for k, v in trait_freq.items() if v > 2]
        return {
            "user_id": user_id,
            "strongest_traits": growth_tags,
            "total_tags": len(trait_freq)
        }
