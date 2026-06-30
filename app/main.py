import os

from dotenv import load_dotenv

from app.agents.manager_agent import ManagerAgent

load_dotenv()

print("=" * 80)
print("🤖 AI Agent System (Day 5: Manager Agent)")
print("=" * 80)

api_key = os.getenv("GROQ_API_KEY")
agent = ManagerAgent(api_key)

print("\n" + "=" * 80)
print("Chat with your AI system! Type 'exit' to quit.")
print("=" * 80)

while True:
    goal = input("\nYou: ").strip()

    if goal.lower() == "exit":
        print("Goodbye!")
        break

    result = agent.run(goal)

    print("\n" + "=" * 80)
    print(f"Final Answer:\n{result}")
    print("=" * 80)