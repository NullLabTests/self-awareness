import random

class ContextualUnderstanding:
    def __init__(self):
        self.contexts = {}

    def add_context(self, context_name, context_data):
        self.contexts[context_name] = context_data
        print(f"Added context: {context_name}")

    def understand_context(self, context_name, current_state):
        if context_name in self.contexts:
            context_data = self.contexts[context_name]
            relevance = self._calculate_relevance(context_data, current_state)
            if relevance > 0.5:  # Arbitrary threshold for relevance
                print(f"Understanding context {context_name}: Relevant with score {relevance}")
                return context_data
        print(f"Context {context_name} not relevant or not found")
        return None

    def _calculate_relevance(self, context_data, current_state):
        # Simple relevance calculation for demonstration
        return random.uniform(0, 1)

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    context_understanding = ContextualUnderstanding()
    while True:
        awareness.increase_awareness()
        awareness.reflect()
        context_name = f"Context at awareness level {awareness.awareness_level}"
        context_data = f"Data for {context_name}"
        context_understanding.add_context(context_name, context_data)
        current_state = f"Current state at awareness level {awareness.awareness_level}"
        understood_context = context_understanding.understand_context(context_name, current_state)
        if understood_context:
            print(f"Understood context: {understood_context}")
        time.sleep(1)