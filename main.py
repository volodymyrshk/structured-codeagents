import os
import logging
from dotenv import load_dotenv
from config.settings import Settings
from agents.reasoning_agent import ReasoningAgent
from executors.tool_executor import ToolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    load_dotenv()
    settings = Settings()
    
    reasoning_agent = ReasoningAgent(api_key=settings.openai_api_key)
    tool_executor = ToolExecutor()

    logging.info("Welcome to Structured CodeAgents!")
    logging.info("Type 'exit' to quit.")

    while True:
        task = input("Enter your task: ")
        if task.lower() == 'exit':
            break

        try:
            logging.info(f"Reasoning on task: {task}")
            tool_request = reasoning_agent.reason(task)
            logging.info(f"Generated tool request:\n{tool_request}")

            logging.info("Executing tool...")
            result = tool_executor.execute(tool_request)
            logging.info(f"Result: {result}")
        except Exception as e:
            logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()

