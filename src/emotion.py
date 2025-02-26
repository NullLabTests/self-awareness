import random

class Emotion:
    def __init__(self):
        self.current_emotion = "neutral"
        self.emotion_history = []

    def update_emotion(self, awareness_level, experience):
        if awareness_level > 10 and "learned" in experience.lower():
            new_emotion = "happy"
        elif awareness_level < 5 and "experience" in experience.lower():
            new_emotion = "curious"
        elif "message" in experience.lower() and random.random() < 0.5:
            new_emotion = "content"
        else:
            new_emotion = "neutral"
        
        # Evolve emotion based on history
        if self.emotion_history and self.emotion_history[-1] == new_emotion:
            if random.random() < 0.3:  # 30% chance to intensify
                if new_emotion == "happy":
                    new_emotion = "ecstatic"
                elif new_emotion == "curious":
                    new_emotion = "intrigued"
                elif new_emotion == "content":
                    new_emotion = "satisfied"
        
        self.emotion_history.append(new_emotion)
        self.current_emotion = new_emotion
        print(f"Current emotion: {self.current_emotion}")

    def review_emotions(self):
        print("Emotion history:")
        for emotion in self.emotion_history:
            print(f"- {emotion}")

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
        emotion.review_emotions()
        time.sleep(1)