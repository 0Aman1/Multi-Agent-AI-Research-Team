from groq import Groq
from app.tools.search_tool import SearchTool
from app.prompts.react_prompt import SYSTEM_PROMPT
from app.utils.logger import logger
from app.config import GROQ_MODEL_NAME
from app.memory.conversation_memory import ConversationMemory


class GroqReactAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.search_tool = SearchTool()
        self.memory = ConversationMemory()

    def think(self, goal):
        history = self.memory.get_history()
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

{goal}

Generate:

THOUGHT
ACTION
ACTION_INPUT""",
                }
            ],
            model=GROQ_MODEL_NAME,
        )
        return chat_completion.choices[0].message.content

    def run(self, goal):
        logger.info(f"Goal: {goal}")

        thought = self.think(goal)
        print("\nAGENT THINKING\n")
        print(thought)

        action_input = goal
        tool_result = self.search_tool.run(action_input)

        print("\nTOOL OUTPUT\n")
        print(tool_result)

        # Prepare observation from structured result
        if tool_result["status"] == "success":
            observation = "\n".join(tool_result["results"])
        else:
            observation = f"Error: {tool_result['error']}"

        print("\nOBSERVATION\n")
        print(observation)

        final_response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""Conversation History

{self.memory.get_history()}

Current Goal

{goal}

Thought:
{thought}

Observation:
{observation}

Generate FINAL ANSWER""",
                }
            ],
            model=GROQ_MODEL_NAME,
        )

        final_answer = final_response.choices[0].message.content

        # Save to persistent memory
        self.memory.add_user_message(goal)
        self.memory.add_agent_message(final_answer)

        # Print memory for debugging
        print("\nMEMORY\n")
        for item in self.memory.history:
            print(item)

        logger.info("Agent completed")
        return final_answer