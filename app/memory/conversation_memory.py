from app.memory.memory_manager import MemoryManager


class ConversationMemory:
    def __init__(self):
        self.manager = MemoryManager()
        self.history = self.manager.load()

    def add_user_message(self, message):
        self.history.append({
            "role": "user",
            "content": message
        })
        self.manager.save(self.history)

    def add_agent_message(self, message):
        self.history.append({
            "role": "assistant",
            "content": message
        })
        self.manager.save(self.history)

    def get_history(self):
        formatted = ""
        for item in self.history:
            formatted += f"{item['role'].upper()}: {item['content']}\n"
        return formatted

    def clear(self):
        self.history = []
        self.manager.clear()