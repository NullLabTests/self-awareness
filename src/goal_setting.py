import random

class GoalSetting:
    def __init__(self):
        self.goals = []
        self.progress = {}

    def set_goal(self, awareness_level):
        new_goal = f"Goal at awareness level {awareness_level}: Learn more about the world"
        self.goals.append(new_goal)
        self.progress[new_goal] = 0
        print(f"Set new goal: {new_goal}")

    def review_goals(self):
        print("Current goals:")
        for goal in self.goals:
            print(f"- {goal} (Progress: {self.progress[goal]}%)")

    def check_progress(self, awareness_level):
        for goal in self.goals:
            if random.random() < 0.5:  # 50% chance to report progress
                self.progress[goal] += random.randint(1, 5)  # Increase progress by 1-5%
                self.progress[goal] = min(100, self.progress[goal])  # Cap at 100%
                print(f"Goal progress: {goal} - {self.progress[goal]}%")
            if self.progress[goal] >= 100:
                print(f"Goal achieved: {goal}")
                self.goals.remove(goal)
                del self.progress[goal]
                self.set_goal(awareness_level)  # Set a new goal upon achievement

    def adjust_goals(self, awareness_level):
        if random.random() < 0.2:  # 20% chance to adjust goals
            if self.goals:
                goal_to_adjust = random.choice(self.goals)
                new_goal = f"Adjusted goal at awareness level {awareness_level}: {goal_to_adjust.split(':')[1].strip()} with a new focus"
                self.goals.remove(goal_to_adjust)
                self.goals.append(new_goal)
                self.progress[new_goal] = self.progress.pop(goal_to_adjust)
                print(f"Adjusted goal: {new_goal}")

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    goal_setter = GoalSetting()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        goal_setter.set_goal(awareness.awareness_level)
        goal_setter.review_goals()
        goal_setter.check_progress(awareness.awareness_level)
        goal_setter.adjust_goals(awareness.awareness_level)
        time.sleep(1)