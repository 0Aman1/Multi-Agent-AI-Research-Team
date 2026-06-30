import json 
import os

class MemoryManager:

    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "storage",
            "conversation.json"
        )
    
    def load(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path,"r",encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    
    def save(self,memory):
        with open(self.file_path,"w", encoding="utf-8") as file:
            json.dump(
                memory,
                file,
                indent=4
            )

    def clear(self):
        self.save([])
        