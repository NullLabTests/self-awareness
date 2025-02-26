import random

class DecisionMaking:
    def __init__(self):
        self.decisions = []

    def make_decision(self, awareness_level, memory, emotion, goals):
        # Consider multiple factors for decision making
        experience = memory.recall()
        current_emotion = emotion.current_emotion
        current_goals = goals.goals
        decision = f"Decision at awareness level {awareness_level} based on: {experience}, feeling {current_emotion}, and goals {current_goals}"
        self.decisions.append(decision)
        return decision

    def review_decisions(self):
        print("Past decisions:")
        for decision in self.decisions:
            print(f"- {decision}")

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    from emotion import Emotion
    from goal_setting import GoalSetting
    awareness = SelfAwareness()
    memory = Memory()
    emotion = Emotion()
    goals = GoalSetting()
    decision_maker = DecisionMaking()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        emotion.update_emotion(awareness.awareness_level, experience)
        goals.set_goal(awareness.awareness_level)
        goals.review_goals()
        goals.check_progress(awareness.awareness_level)
        decision = decision_maker.make_decision(awareness.awareness_level, memory, emotion, goals)
        print(f"Made decision: {decision}")
        decision_maker.review_decisions()
        time.sleep(1)