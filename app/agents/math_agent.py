from app.tools.tool_registry import ToolRegistry

class MathAgent:

    def __init__(self):
        self.registry = ToolRegistry()
    
    def run(self,goal):
        calculator = self.registry.get_tool("calculator")
        result = calculator.run(goal)
        return f"Math Result:\n{result}"
