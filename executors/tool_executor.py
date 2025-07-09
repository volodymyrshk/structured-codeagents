import json
from tools import math_tools

class ToolExecutor:
    def __init__(self):
        self.tools = {
            "calculate_derivative": math_tools.calculate_derivative,
            "calculate_integral": math_tools.calculate_integral,
            "solve_equation": math_tools.solve_equation,
        }

    def execute(self, tool_request: str):
        try:
            request = json.loads(tool_request)
            tool_name = request["tool"]
            args = request["args"]

            if tool_name in self.tools:
                return self.tools[tool_name](**args)
            else:
                return f"Error: Tool '{tool_name}' not found."
        except json.JSONDecodeError:
            return "Error: Invalid JSON format from the agent."
        except Exception as e:
            return f"An error occurred during execution: {e}"
