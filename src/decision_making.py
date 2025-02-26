import random

class DecisionMaking:
    def __init__(self):
        self.decisions = []

    def make_decision(self, awareness_level, memory):
        # Simple decision making based on awareness level and a random past experience
        experience = memory.recall()
        decision = f"Decision at awareness level {awareness_level} based on: {experience}"
        self.decisions.append(decision)
        return decision

    def review_decisions(self):
        print("Past decisions:")
        for decision in self.decisions:
            print(f"- {decision}")

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    awareness = SelfAwareness()
    memory = Memory()
    decision_maker = DecisionMaking()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        decision = decision_maker.make_decision(awareness.awareness_level, memory)
        print(f"Made decision: {decision}")
        decision_maker.review_decisions()
        time.sleep(1)