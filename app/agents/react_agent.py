from google import genai

from app.tools.search_tool import SearchTool
from app.tools.tool_registry import ToolRegistry
from app.prompts.react_prompt import SYSTEM_PROMPT
from app.utils.logger import logger
from app.config import MODEL_NAME
from app.memory.memory import Memory
from app.memory.conversation import format_history

class ReactAgent:
    def __init__(self, api_key):
        self.client = genai.Client(
            api_key =api_key
        )
        self.search_tool = SearchTool()
        self.tool_registry = ToolRegistry()
    def choose_tool(self,goal):
        goal = goal.lower()
        math_keywords = [
            "+","-","*","/","calculate"
        ]

        if any(
            keyword in goal
            for keyword in math_keywords           
       ):
            return "calculator"
        return "search"

    def think(self,goal):
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=f"""
Goal:

{goal}

Generate:

THOUGHT
ACTION
ACTION_INPUT
"""

        )
        return response.text
    
    def run(self,goal):
        logger.info(f"Goal: {goal}")
        thought =self.think(goal)
        print("\nAGENT THINKING\n")
        print(thought)

        action_input = goal
        tool_name =self.choose_tool(goal)
        tool =self.tool_registry.get_tool(
            tool_name
        )
        print(f"\nTOOL SELECTED: {tool_name}\n")
        observation = tool.run(
            action_input
        )

        print("\nOBSERVATION\n")
        print(observation)

        final_response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=f"""
Goal:
{goal}

Thought:
{thought}

Observation:
{observation}

Generate FINAL ANSWER
"""
        )
        logger.info("Agent completed")
        return final_response.text