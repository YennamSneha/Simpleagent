import subprocess
import os
import webbrowser


def run_python_file(filename):

    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Python program timed out."
        }


def run_java_file(filename):

    try:
        classname = os.path.splitext(os.path.basename(filename))[0]
        folder = os.path.dirname(filename)

        compile_result = subprocess.run(
            ["javac", filename],
            capture_output=True,
            text=True,
            timeout=15
        )

        if compile_result.returncode != 0:
            return {
                "success": False,
                "error": compile_result.stderr
            }

        run_result = subprocess.run(
            ["java", "-cp", folder, classname],
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "success": run_result.returncode == 0,
            "output": run_result.stdout,
            "error": run_result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Java program timed out."
        }


def run_c_file(filename):

    try:
        exe = filename.replace(".c", ".exe")

        compile_result = subprocess.run(
            ["gcc", filename, "-o", exe],
            capture_output=True,
            text=True,
            timeout=20
        )

        if compile_result.returncode != 0:
            return {
                "success": False,
                "error": compile_result.stderr
            }

        run_result = subprocess.run(
            [exe],
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "success": run_result.returncode == 0,
            "output": run_result.stdout,
            "error": run_result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "C program timed out."
        }


def run_js_file(filename):

    try:
        result = subprocess.run(
            ["node", filename],
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "JavaScript program timed out."
        }


def run_html_file(filename):

    try:
        webbrowser.open(os.path.abspath(filename))

        return {
            "success": True,
            "output": "HTML file opened in your default browser."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def run_file(filename):

    extension = os.path.splitext(filename)[1].lower()

    if extension == ".py":
        return run_python_file(filename)

    elif extension == ".java":
        return run_java_file(filename)
    elif extension == ".c":
        return run_c_file(filename)

    elif extension == ".js":
        return run_js_file(filename)

    elif extension == ".html":
        return run_html_file(filename)

    else:
        return {
            "success": False,
            "error": f"{extension} files are not supported."
        }