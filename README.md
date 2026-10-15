Week 2 – Core Agent Loop

Project Overview

The Core Agent Loop is a Python-based project that demonstrates how an AI agent can receive tasks, process them, execute actions, and record results. It provides a simple structure for understanding task execution, logging, and testing in an agent-based system.

Objectives

- Build a basic agent loop for processing tasks.
- Implement task execution using Python.
- Support even and odd number task operations.
- Maintain logs for monitoring execution.
- Write tests to verify the agent's functionality.

Technologies Used

- Python
- Pytest
- Logging
- Git and GitHub

Project Structure

week2-CoreAgentLoop/

├── logs
├── tests
├── .env.example
├── .gitignore
├── README.md
├── agent.py
├── demo_task.txt
├── execute.py
├── executor.py
├── llm.py
├── logger.py
├── requirements.txt
└── run_tests.py

Key Features

- Task Processing: Accepts and processes tasks through the agent loop.
- Task Execution: Executes supported operations using Python.
- Logging: Records execution information for debugging and monitoring.
- Testing: Includes test files to check the behavior of the application.
- Configuration: Uses an example environment file for configuration.

Installation and Setup

1. Clone the repository:
   
   git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder:
   
   cd week2-CoreAgentLoop

3. Create a virtual environment:
   
   python3 -m venv venv

4. Activate the environment:
   
   macOS/Linux
   
   source venv/bin/activate
   
   Windows
   
   venv\Scripts\activate

5. Install dependencies:
   
   pip install -r requirements.txt

How to Run

Run the main agent:

python agent.py

Run the test suite:

python run_tests.py

Note: Use the actual entry-point and test commands defined in your project if they differ.

Learning Outcomes

- Understanding the core loop of an AI agent.
- Organizing Python projects into reusable modules.
- Handling task execution and logging.
- Writing and running tests.
- Managing projects using GitHub.

Conclusion

This project demonstrates the fundamentals of a Python-based agent loop, including task processing, execution, logging, and testing. It serves as a foundation for building more advanced AI agent applications.
