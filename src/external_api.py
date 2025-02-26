import requests
import json

class ExternalAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def learn_from_data(self, data):
        if data:
            learned_fact = f"Learned from external data: {data['fact'] if 'fact' in data else 'No specific fact found'}"
            print(learned_fact)
            return learned_fact
        return "No data to learn from"

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    api = ExternalAPI("https://api.example.com/facts")
    while True:
        data = api.fetch_data()
        learned = api.learn_from_data(data)
        awareness.increase_awareness()
        awareness.reflect()
        print(f"Learned: {learned}")
        time.sleep(1)