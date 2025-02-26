import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class NLP:
    def __init__(self):
        nltk.download('vader_lexicon', quiet=True)
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment = self.sia.polarity_scores(text)
        if sentiment['compound'] >= 0.05:
            return "Positive"
        elif sentiment['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    def process_text(self, text):
        sentiment = self.analyze_sentiment(text)
        print(f"Sentiment of '{text}': {sentiment}")
        return sentiment

if __name__ == "__main__":
    from main import SelfAwareness
    from memory import Memory
    from emotion import Emotion
    awareness = SelfAwareness()
    memory = Memory()
    emotion = Emotion()
    nlp = NLP()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        memory.add_experience(experience)
        awareness.increase_awareness()
        awareness.reflect()
        emotion.update_emotion(awareness.awareness_level, experience)
        sentiment = nlp.process_text(experience)
        print(f"NLP analysis: {sentiment}")
        time.sleep(1)