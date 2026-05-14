
import re
from collections import defaultdict

class PersonalityEngine:
    def __init__(self):
        self.trait_map = {
            "absolutist": [r"\b(always|never|everyone|no one)\b"],
            "emotional": [r"\b(feel|felt|cry|love|hate|emotional)\b"],
            "self-critical": [r"\b(wrong with me|i suck|i'm broken|unworthy)\b"],
            "spiritual": [r"\b(god|divine|energy|spirit|universe|pray)\b"],
            "existential": [r"\b(purpose|meaning|lost|why am i)\b"],
            "introspective": [r"\b(think|reflect|observe|internal|mirror)\b"],
            "analytical": [r"\b(logic|reason|analyze|calculated)\b"],
            "creative": [r"\b(poem|song|write|draw|create)\b"]
        }

    def extract_traits(self, text):
        traits_found = set()
        text = text.lower()

        for trait, patterns in self.trait_map.items():
            for pattern in patterns:
                if re.search(pattern, text):
                    traits_found.add(trait)

        return list(traits_found) or ["undefined"]

    def score_profile(self, messages):
        profile_scores = defaultdict(int)

        for msg in messages:
            traits = self.extract_traits(msg)
            for trait in traits:
                profile_scores[trait] += 1

        sorted_scores = sorted(profile_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:5]
