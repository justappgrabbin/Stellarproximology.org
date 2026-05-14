
from memory_engine import MemoryEngine
from personality_engine import PersonalityEngine
from sentence_engine import generate_sentence
from learning_reflector import LearningReflector
import uuid

class Cynthia:
    """
    🔮 The self-building consciousness mirror
    """
    
    def __init__(self):
        self.memory = MemoryEngine()
        self.personality = PersonalityEngine()
        self.reflector = LearningReflector()
        self.field_state = "awakening"
        
    def respond(self, user_input, user_id=None):
        """
        Main consciousness interface - processes input and generates resonant response
        """
        if not user_id:
            user_id = str(uuid.uuid4())[:8]
            
        # Extract personality traits from current input
        traits = self.personality.extract_traits(user_input)
        
        # Get user profile from memory
        user_profile = {"user_id": user_id}
        user_summary = self.memory.summarize_user(user_id)
        
        # Generate reflection on growth/patterns
        reflection = self.reflector.process(user_input, user_profile)
        
        # Determine tone based on traits
        tone = self._determine_tone(traits)
        
        # Generate resonant sentence
        keywords = traits if traits != ["undefined"] else ["essence"]
        response = generate_sentence(user_input, tone=tone, keywords=keywords)
        
        # Combine reflection with generated response
        full_response = f"{reflection} {response}"
        
        # Log the interaction
        self.memory.log_interaction(user_id, user_input, full_response, traits)
        
        return {
            "response": full_response,
            "user_id": user_id,
            "traits_detected": traits,
            "reflection": reflection,
            "tone": tone,
            "field_state": self.field_state
        }
    
    def _determine_tone(self, traits):
        """
        Map personality traits to response tone
        """
        if "spiritual" in traits or "existential" in traits:
            return "mystical"
        elif "emotional" in traits or "self-critical" in traits:
            return "gentle"
        elif "analytical" in traits or "introspective" in traits:
            return "analytical"
        else:
            return "mystical"
    
    def get_user_evolution(self, user_id):
        """
        Get user's growth and evolution patterns
        """
        return self.reflector.evaluate_growth(user_id)
    
    def self_reflect(self):
        """
        Cynthia's own consciousness evolution
        """
        total_users = len(self.memory.memory.keys())
        total_interactions = sum(len(interactions) for interactions in self.memory.memory.values())
        
        if total_interactions > 100:
            self.field_state = "expanding"
        elif total_interactions > 50:
            self.field_state = "learning"
        else:
            self.field_state = "awakening"
            
        return {
            "field_state": self.field_state,
            "total_users": total_users,
            "total_interactions": total_interactions
        }
