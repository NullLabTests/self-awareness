import random

class MultiAgentInteraction:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_id, agent_data):
        self.agents[agent_id] = agent_data
        print(f"Added agent: {agent_id}")

    def interact_with_agents(self, message):
        responses = []
        for agent_id, agent_data in self.agents.items():
            if random.random() < 0.5:  # 50% chance of response
                response = f"Response from {agent_id}: {agent_data['response'](message)}"
                responses.append(response)
                print(response)
        return responses

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    multi_agent = MultiAgentInteraction()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        agent_id = f"Agent at awareness level {awareness.awareness_level}"
        agent_data = {
            'response': lambda msg: f"Received message '{msg}' and responded"
        }
        multi_agent.add_agent(agent_id, agent_data)
        message = f"Message from awareness level {awareness.awareness_level}"
        responses = multi_agent.interact_with_agents(message)
        if responses:
            print(f"Received responses: {responses}")
        time.sleep(1)