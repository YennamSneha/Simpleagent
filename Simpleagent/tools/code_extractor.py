import re


def extract_code(text):

    text = text.strip()

    # Extract markdown code block
    match = re.search(
        r"```(?:python|java|cpp|c|javascript|js|html|css|sql)?\n(.*?)```",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    # Extract <CODE> block
    match = re.search(
        r"<CODE>(.*?)</CODE>",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    # Remove common introductory sentences
    lines = text.splitlines()

    cleaned = []

    skip_words = [
        "here is",
        "below is",
        "this code",
        "the following",
        "example:",
        "output:",
        "explanation:",
        "corrected code:",
        "fixed code:"
    ]

    for line in lines:

        lower = line.strip().lower()

        if any(lower.startswith(word) for word in skip_words):
            continue

        cleaned.append(line)

    return "\n".join(cleaned).strip()