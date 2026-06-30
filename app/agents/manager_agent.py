from app.agents.groq_react_agent import GroqReactAgent
from app.agents.math_agent import MathAgent


class ManagerAgent:
    def __init__(self, api_key):
        self.research_agent = GroqReactAgent(api_key)
        self.math_agent = MathAgent()

    def decide(self, goal):
        goal = goal.lower()
        math_symbols = ["+", "-", "*", "/", "%", "(", ")"]
        if any(symbol in goal for symbol in math_symbols):
            return "math"
        return "research"

    def run(self, goal):
        agent = self.decide(goal)
        print(f"\nMANAGER ROUTED TO: {agent.upper()} AGENT\n")
        if agent == "math":
            return self.math_agent.run(goal)
        return self.research_agent.run(goal)