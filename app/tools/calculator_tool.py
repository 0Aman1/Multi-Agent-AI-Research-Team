from app.tools.base_tool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"

    def run(self,expression):
        try: 
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calcution Error: {e}"