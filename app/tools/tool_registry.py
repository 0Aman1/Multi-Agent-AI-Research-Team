from app.tools.search_tool import SearchTool
from app.tools.calculator_tool import CalculatorTool

class ToolRegistry:
    def __init__(self):
        self.tools={
            "search": SearchTool(),
            "calculator": CalculatorTool()
        }

    def get_tool(self,tool_name):
        return self.tools.get(tool_name)

    def list_tool(self):
        return list(self.tools.keys())