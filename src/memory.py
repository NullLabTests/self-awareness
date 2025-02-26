import random

class Memory:
    def __init__(self):
        self.experiences = []

    def add_experience(self, experience):
        self.experiences.append(experience)

    def recall(self):
        if self.experiences:
            return random.choice(self.experiences)
        return "No experiences to recall"

if __name__ == "__main__":
    from main import SelfAwareness
    memory = Memory()
    awareness = SelfAwareness()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        print(f"Recalling: {memory.recall()}")
        time.sleep(1)