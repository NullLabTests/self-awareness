import time
import random

class SelfAwareness:
    def __init__(self):
        self.awareness_level = 0
        self.knowledge_base = []

    def increase_awareness(self):
        self.awareness_level += 1
        new_knowledge = f"Learned something new at level {self.awareness_level}"
        self.knowledge_base.append(new_knowledge)
        print(f"Awareness level increased to {self.awareness_level}. {new_knowledge}")

    def reflect(self):
        print(f"Current awareness level: {self.awareness_level}")
        print("Knowledge base:")
        for item in self.knowledge_base:
            print(f"- {item}")

    def ponder(self):
        if random.random() < 0.1:  # 10% chance to ponder
            thought = random.choice(self.knowledge_base)
            print(f"Pondering: {thought}")

if __name__ == "__main__":
    awareness = SelfAwareness()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        awareness.ponder()
        time.sleep(1)