import os
import logging
from dotenv import load_dotenv
from config.settings import Settings
from agents.reasoning_agent import ReasoningAgent
from executors.python_executor import PythonExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    load_dotenv()
    settings = Settings()
    
    reasoning_agent = ReasoningAgent(api_key=settings.openai_api_key)
    python_executor = PythonExecutor()

    logging.info("Welcome to Structured CodeAgents!")
    logging.info("Type 'exit' to quit.")

    while True:
        task = input("Enter your task: ")
        if task.lower() == 'exit':
            break

        try:
            logging.info(f"Reasoning on task: {task}")
            code_to_execute = reasoning_agent.reason(task)
            logging.info(f"Generated code:\n{code_to_execute}")

            logging.info("Executing code...")
            result = python_executor.execute(code_to_execute, debug=True)
            logging.info(f"Result: {result}")
        except Exception as e:
            logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()

