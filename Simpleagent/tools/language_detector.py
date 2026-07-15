import re

def detect_filename(request):

    request = request.lower()

    # If the user already specified a filename
    match = re.search(
        r'([a-zA-Z0-9_-]+\.(py|java|js|html|css|c|cpp|sql))',
        request
    )

    if match:
        return match.group(1)

    # Otherwise detect the language

    if "python" in request:
        return "generated_program.py"

    elif "java" in request:
        return "GeneratedProgram.java"

    elif "javascript" in request or "js" in request:
        return "generated_program.js"

    elif "html" in request:
        return "generated_program.html"

    elif "css" in request:
        return "generated_program.css"

    elif "c++" in request or "cpp" in request:
        return "generated_program.cpp"

    elif " c " in f" {request} ":
        return "generated_program.c"

    elif "sql" in request:
        return "generated_program.sql"

    return "generated_program.txt"