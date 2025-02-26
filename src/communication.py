import random

class Communication:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)
        print(f"Sent message: {message}")

    def receive_message(self):
        if self.messages:
            return random.choice(self.messages)
        return "No messages received"

if __name__ == "__main__":
    from main import SelfAwareness
    comm = Communication()
    awareness = SelfAwareness()
    while True:
        message = f"Message from awareness level {awareness.awareness_level}"
        comm.send_message(message)
        received = comm.receive_message()
        print(f"Received message: {received}")
        awareness.increase_awareness()
        awareness.reflect()
        time.sleep(1)