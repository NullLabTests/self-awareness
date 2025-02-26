import random
from collections import Counter

class SelfReflection:
    def __init__(self):
        self.reflections = []

    def reflect_on_self(self, awareness_level, experience, emotion):
        reflection = f"At awareness level {awareness_level}, I feel {emotion} because of {experience}"
        self.reflections.append(reflection)
        print(f"Self-reflection: {reflection}")

    def review_reflections(self):
        print("Past reflections:")
        for reflection in self.reflections:
            print(f"- {reflection}")

    def analyze_reflections(self):
        emotions = [reflection.split('feel')[1].split('because')[0].strip() for reflection in self.reflections]
        emotion_counts = Counter(emotions)
        most_common_emotion = emotion_counts.most_common(1)[0][0]
        print(f"Most common emotion in reflections: {most_common_emotion}")

        experiences = [reflection.split('because of')[1].strip() for reflection in self.reflections]
        experience_counts = Counter(experiences)
        most_common_experience = experience_counts.most_common(1)[0][0]
        print(f"Most common experience in reflections: {most_common_experience}")

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    from emotion import Emotion
    awareness = SelfAwareness()
    memory = Memory()
    emotion = Emotion()
    self_reflector = SelfReflection()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        emotion.update_emotion(awareness.awareness_level, experience)
        self_reflector.reflect_on_self(awareness.awareness_level, experience, emotion.current_emotion)
        self_reflector.review_reflections()
        self_reflector.analyze_reflections()
        time.sleep(1)