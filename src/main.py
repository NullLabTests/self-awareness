import time

class SelfAwareness:
    def __init__(self):
        self.awareness_level = 0

    def increase_awareness(self):
        self.awareness_level += 1
        print(f"Awareness level increased to {self.awareness_level}")

    def reflect(self):
        print(f"Current awareness level: {self.awareness_level}")

if __name__ == "__main__":
    awareness = SelfAwareness()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        time.sleep(1)