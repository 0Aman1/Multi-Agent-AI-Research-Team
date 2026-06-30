import google.generativeai as genai

from app.prompts.agent_prompt import SYSTEM_PROMPT
from app.utils.logger import logger


class ResearchAgent:

    def __init__(self, api_key):

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_PROMPT
        )

    def run(self, goal: str):

        logger.info(f"Received Goal: {goal}")

        response = self.model.generate_content(goal)

        logger.info("Agent execution completed")

        return response.text