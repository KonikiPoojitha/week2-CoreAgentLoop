from llm import ask_llm
from executor import execute_code
from logger import log_attempt


MAX_ATTEMPTS = 3


def run_agent(task):
    print("\n=== CORE AGENT LOOP ===")
    print(f"Task: {task}\n")

    prompt = f"""
You are a Python coding agent.

User task:
{task}

Return ONLY Python code.
The code must directly solve the task.
Include an assertion that verifies the expected result.

Do not use shell commands.
Do not use eval() or exec().
"""

    for attempt in range(1, MAX_ATTEMPTS + 1):

        print(f"\n--- Attempt {attempt}/{MAX_ATTEMPTS} ---")

        code = ask_llm(prompt)

        print("\nGenerated code:")
        print(code)

        result = execute_code(code, timeout=10)

        print("\nExecution result:")

        if result["success"]:
            print(result["output"])
            print("PASS")

            log_attempt(
                attempt=attempt,
                code=code,
                result=result,
                passed=True
            )

            return True

        else:
            print(result["error"])
            print("FAILED")

            log_attempt(
                attempt=attempt,
                code=code,
                result=result,
                passed=False
            )

            if attempt < MAX_ATTEMPTS:
                prompt = f"""
The previous Python code failed.

Original task:
{task}

Previous code:
{code}

Error:
{result["error"]}

Fix the code and return ONLY the corrected Python code.

Do not use eval() or exec().
Make sure the corrected code includes an assertion
that verifies the expected result.
"""

    print("\nAgent failed after 3 attempts.")
    return False


if __name__ == "__main__":
    task = input("Enter your task: ")
    run_agent(task)
