from groq import Groq
from app.prompts.agent_prompt import SYSTEM_PROMPT
from app.utils.logger import logger
from app.config import GROQ_MODEL_NAME
from app.memory.memory import Memory
from app.memory.conversation import format_history


class GroqResearchAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.memory = Memory()

    def run(self, goal: str):
        logger.info(f"Received Goal: {goal}")
        self.memory.add("user", goal)

        history = format_history(self.memory.get_history())
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""Conversation History

{history}

Current Goal

{goal}""",
                }
            ],
            model=GROQ_MODEL_NAME,
        )

        response_text = chat_completion.choices[0].message.content
        self.memory.add("agent", response_text)

        # Print memory for debugging
        print("\nMEMORY\n")
        for item in self.memory.get_history():
            print(item)

        logger.info("Groq Agent execution completed")
        return response_text