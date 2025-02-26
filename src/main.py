import time
import random
from visualization import Visualization
from ml_adaptation import MLAdaptation
from memory import Memory

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
    viz = Visualization()
    ml = MLAdaptation()
    memory = Memory()
    while True:
        external_input = random.uniform(0, 1)  # Simulating external input
        new_awareness = ml.adapt_awareness(awareness.awareness_level, external_input)
        error = new_awareness - awareness.awareness_level
        ml.update_weights(error)
        awareness.awareness_level = new_awareness
        awareness.increase_awareness()
        awareness.reflect()
        awareness.ponder()
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        print(f"Recalling: {memory.recall()}")
        viz.draw(awareness.awareness_level)
        time.sleep(1)