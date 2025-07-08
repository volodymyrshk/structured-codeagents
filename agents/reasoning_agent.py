import logging
from openai import OpenAI

class ReasoningAgent:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def reason(self, task: str) -> str:
        logging.info(f"ReasoningAgent: Received task: {task}")
        prompt = f"""You are an AI assistant that generates Python code to solve mathematical problems. 
        The user will provide a task, and you should output only the Python code that solves it. 
        Do not include any explanations or extra text, just the code. 
        Make sure the code is executable and prints the result.
        
        Example:
        Task: What is the derivative of x^2?
        Code: 
from sympy import symbols, diff
x = symbols('x')
expr = x**2
derivative = diff(expr, x)
print(derivative)

        Task: {task}
        Code:
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
