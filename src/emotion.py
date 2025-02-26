import random

class Emotion:
    def __init__(self):
        self.current_emotion = "neutral"

    def update_emotion(self, awareness_level, experience):
        if awareness_level > 10 and "learned" in experience.lower():
            self.current_emotion = "happy"
        elif awareness_level < 5 and "experience" in experience.lower():
            self.current_emotion = "curious"
        else:
            self.current_emotion = "neutral"
        print(f"Current emotion: {self.current_emotion}")

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    awareness = SelfAwareness()
    memory = Memory()
    emotion = Emotion()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        emotion.update_emotion(awareness.awareness_level, experience)
        time.sleep(1)