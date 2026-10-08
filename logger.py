import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "agent.log")


def log_attempt(attempt, code, result, passed):
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Attempt: {attempt}\n")
        file.write(f"Passed: {passed}\n")

        file.write("\n--- CODE ---\n")
        file.write(code)

        file.write("\n--- OUTPUT ---\n")
        file.write(result.get("output", ""))

        file.write("\n--- ERROR ---\n")
        file.write(result.get("error", ""))

        file.write("\n--- RETURN CODE ---\n")
        file.write(str(result.get("returncode", "")))

        file.write("\n")
