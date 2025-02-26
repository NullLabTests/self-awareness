import random
import time

class RealTimeData:
    def __init__(self):
        self.data_stream = []

    def generate_data(self):
        # Simulate real-time data generation
        data_point = random.uniform(0, 1)
        self.data_stream.append(data_point)
        print(f"Generated real-time data: {data_point}")
        return data_point

    def process_data(self, data_point, awareness_level):
        if data_point > 0.7:
            print(f"Reacting to high data point {data_point} at awareness level {awareness_level}")
            return f"Reacted to high data at level {awareness_level}"
        return None

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    real_time = RealTimeData()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        data_point = real_time.generate_data()
        reaction = real_time.process_data(data_point, awareness.awareness_level)
        if reaction:
            print(f"Real-time reaction: {reaction}")
        time.sleep(1)