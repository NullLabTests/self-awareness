import random

class SocialInteraction:
    def __init__(self):
        self.social_cues = []
        self.learned_behaviors = []

    def receive_social_cue(self, cue):
        self.social_cues.append(cue)
        print(f"Received social cue: {cue}")

    def learn_from_cue(self, cue):
        if random.random() < 0.5:  # 50% chance to learn
            learned_behavior = f"Learned behavior from cue: {cue}"
            self.learned_behaviors.append(learned_behavior)
            print(f"Learned behavior: {learned_behavior}")
            return learned_behavior
        return None

    def interact(self, message):
        response = f"Response to '{message}': {random.choice(self.learned_behaviors) if self.learned_behaviors else 'No learned behaviors yet'}"
        print(response)
        return response

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    awareness = SelfAwareness()
    memory = Memory()
    social = SocialInteraction()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        social_cue = f"Social cue at awareness level {awareness.awareness_level}"
        social.receive_social_cue(social_cue)
        learned = social.learn_from_cue(social_cue)
        if learned:
            memory.add_experience(learned)
        social.interact(experience)
        time.sleep(1)