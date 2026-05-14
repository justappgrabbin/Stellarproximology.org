import json
from datetime import datetime
from collections import defaultdict

class MemoryEngine:
    def __init__(self, memory_file='cynthia_memory.json'):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return defaultdict(list)

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def log_interaction(self, user_id, prompt, response, tags=None):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "response": response,
            "tags": tags or []
        }

        # Initialize user memory if it doesn't exist
        if user_id not in self.memory:
            self.memory[user_id] = []

        self.memory[user_id].append(log_entry)
        self.save_memory()

    def get_recent_memories(self, user_id, n=5):
        return self.memory.get(user_id, [])[-n:]

    def extract_keywords(self, text):
        # Placeholder for future NLP-based keyword extraction
        return list(set(text.lower().split()))

    def summarize_user(self, user_id):
        memories = self.memory.get(user_id, [])
        if not memories:
            return "No memories yet."

        summary = {
            "total_interactions": len(memories),
            "recent_topics": [],
            "common_words": defaultdict(int),
        }

        for entry in memories[-10:]:
            words = self.extract_keywords(entry['prompt'] + " " + entry['response'])
            for word in words:
                summary["common_words"][word] += 1
            summary["recent_topics"].append(entry['tags'])

        sorted_keywords = sorted(summary["common_words"].items(), key=lambda x: x[1], reverse=True)
        summary["top_keywords"] = [kw for kw, _ in sorted_keywords[:5]]
        return summary

    def get_user_tags(self, user_id):
        tag_set = set()
        for entry in self.memory.get(user_id, []):
            tag_set.update(entry.get("tags", []))
        return list(tag_set)

    def get_user_profile(self, user_id):
        """Get user profile and conversation history"""
        if user_id not in self.memory:
            self.memory[user_id] = []
            return {"new_user": True, "interactions": []}

        interactions = self.memory[user_id]

# Example usage:
# mem = MemoryEngine()
# mem.log_interaction("adayaverse", "Who am I?", "You are a resonance mirror.", tags=["identity", "initiation"])
# print(mem.summarize_user("adayaverse"))