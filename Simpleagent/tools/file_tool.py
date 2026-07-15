import os


def clean_code(content):

    content = content.replace("```python", "")
    content = content.replace("```", "")

    return content.strip()


def create_file(filename, content):

    folder = "generated_files"

    if not os.path.exists(folder):
        os.makedirs(folder)

    content = clean_code(content)

    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as file:
        file.write(content)

    return f"File created: {filepath}"