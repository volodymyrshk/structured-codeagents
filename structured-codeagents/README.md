# Structured CodeAgents

This project demonstrates a structured approach to building AI agents that can reason and execute code for computational tasks. It uses an OpenAI LLM to generate Python code based on a given task, and then safely executes that code to provide a result.

## Features

- **Reasoning Agent**: Leverages OpenAI's GPT models to understand natural language tasks and generate executable Python code.
- **Python Executor**: Safely executes the generated Python code.
- **Mathematical Tools**: Integrates with `sympy` for symbolic mathematics (e.g., derivatives, integrals, equation solving).
- **Logging**: Basic logging implemented to track execution flow and errors.
- **Debugging**: Enhanced error reporting for code execution.

## Project Structure

```
structured-codeagents/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── main.py
├── config/
│   └── settings.py
├── agents/
│   ├── __init__.py
│   └── reasoning_agent.py
├── executors/
│   ├── __init__.py
│   └── python_executor.py
├── tools/
│   ├── __init__.py
│   └── math_tools.py
└── venv/ (Python virtual environment)
```

## Setup

1.  **Clone the repository (or create the files manually):**

    ```bash
    git clone <your-repo-url>
    cd structured-codeagents
    ```

2.  **Create a Python Virtual Environment and Install Dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Configure OpenAI API Key:**

    Copy the `.env.example` file to `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key.

    ```bash
    cp .env.example .env
    ```

    Open the newly created `.env` file and add your API key:

    ```
    OPENAI_API_KEY=sk-your_openai_api_key_here
    ```

## Usage

1.  **Activate the virtual environment:**

    ```bash
    source venv/bin/activate
    ```

2.  **Run the main application:**

    ```bash
    python main.py
    ```

3.  **Enter your tasks:**

    The application will prompt you to enter a task. For example:

    ```
    Enter your task: What is the derivative of x^2?
    ```

    The agent will then reason, generate code, execute it, and print the result.

    Type `exit` to quit the application.

## Example Tasks

-   `What is the derivative of x^2?`
-   `Solve 4x^2 + 4x - 4 = 0`
-   `Integrate sin(x)`
