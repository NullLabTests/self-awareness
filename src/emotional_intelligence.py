import random

class EmotionalIntelligence:
    def __init__(self):
        self.emotion_history = []
        self.emotion_map = {
            "happy": ["joyful", "ecstatic", "content"],
            "sad": ["upset", "depressed", "disappointed"],
            "angry": ["irritated", "furious", "annoyed"],
            "fearful": ["anxious", "scared", "nervous"],
            "neutral": ["calm", "indifferent", "unaffected"]
        }

    def recognize_emotion(self, text):
        for emotion, synonyms in self.emotion_map.items():
            for synonym in synonyms:
                if synonym in text.lower():
                    self.emotion_history.append(emotion)
                    print(f"Recognized emotion: {emotion}")
                    return emotion
        return "neutral"

    def respond_to_emotion(self, emotion):
        if emotion in self.emotion_map:
            response = f"Responding to {emotion} emotion: I understand you feel {random.choice(self.emotion_map[emotion])}."
            print(response)
            return response
        return "I'm not sure how to respond to that emotion."

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    emotional_intelligence = EmotionalIntelligence()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        experience = f"Experience at awareness level {awareness.awareness_level}"
        recognized_emotion = emotional_intelligence.recognize_emotion(experience)
        response = emotional_intelligence.respond_to_emotion(recognized_emotion)
        print(f"Emotional response: {response}")
        time.sleep(1)