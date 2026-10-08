import subprocess
import tempfile
from pathlib import Path
import sys


def execute_code(code: str, timeout: int = 10) -> dict:
    """
    Execute generated Python code in a separate process
    with a timeout and captured output.
    """

    with tempfile.TemporaryDirectory(prefix="agent_run_") as tmp:
        script = Path(tmp) / "generated_code.py"

        script.write_text(code, encoding="utf-8")

        try:
            completed = subprocess.run(
                [sys.executable, str(script)],
                cwd=tmp,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            return {
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "timed_out": False,
            }

        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""

            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")

            if isinstance(stderr, bytes):
                stderr = stderr.decode("utf-8", errors="replace")

            return {
                "returncode": -1,
                "stdout": stdout,
                "stderr": (
                    f"Execution timed out after {timeout} seconds.\n"
                    f"{stderr}"
                ),
                "timed_out": True,
            }

