import subprocess
import sys
import tempfile
import os


def execute_code(code, timeout=10):
    """
    Safely execute generated Python code in a temporary file.
    Returns success, output, and error information.
    """

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": f"Execution timed out after {timeout} seconds.",
            "returncode": -1
        }

    except Exception as e:
        return {
            "success": False,
            "output": "",
            "error": str(e),
            "returncode": -1
        }

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
