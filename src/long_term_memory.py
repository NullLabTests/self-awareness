import sqlite3
import time

class LongTermMemory:
    def __init__(self, db_name='long_term_memory.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS memories
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             timestamp REAL,
                             content TEXT)''')
        self.conn.commit()

    def store_memory(self, content):
        timestamp = time.time()
        self.cursor.execute("INSERT INTO memories (timestamp, content) VALUES (?, ?)", (timestamp, content))
        self.conn.commit()
        print(f"Stored memory: {content}")

    def retrieve_memory(self, time_threshold=3600):  # Default to 1 hour
        current_time = time.time()
        self.cursor.execute("SELECT content FROM memories WHERE timestamp > ? ORDER BY timestamp DESC LIMIT 1", (current_time - time_threshold,))
        memory = self.cursor.fetchone()
        if memory:
            print(f"Retrieved memory: {memory[0]}")
            return memory[0]
        return None

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    from main import SelfAwareness
    awareness = SelfAwareness()
    ltm = LongTermMemory()
    while True:
        experience = f"Experience at awareness level {awareness.awareness_level}"
        ltm.store_memory(experience)
        awareness.increase_awareness()
        awareness.reflect()
        retrieved = ltm.retrieve_memory()
        if retrieved:
            print(f"Long-term memory recall: {retrieved}")
        time.sleep(1)
    ltm.close()