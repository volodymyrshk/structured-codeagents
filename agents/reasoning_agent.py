import logging
from openai import OpenAI

class ReasoningAgent:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def reason(self, task: str) -> str:
        logging.info(f"ReasoningAgent: Received task: {task}")
        prompt = f"""You are an AI assistant that uses tools to solve mathematical problems.
        Based on the user's task, you should select a tool and provide the necessary arguments in JSON format.

        Available tools:
        - calculate_derivative(expression_str: str, variable_str: str)
        - calculate_integral(expression_str: str, variable_str: str)
        - solve_equation(equation_str: str, variable_str: str)

        Example:
        Task: What is the derivative of x^2 with respect to x?
        {{
            "tool": "calculate_derivative",
            "args": {{
                "expression_str": "x**2",
                "variable_str": "x"
            }}
        }}

        Task: {task}
        """
        
        logging.info("ReasoningAgent: Sending request to OpenAI API...")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can choose a different model if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates Python code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0
        )
        
        code = response.choices[0].message.content.strip()
        logging.info("ReasoningAgent: Received response from OpenAI API.")
        return code
