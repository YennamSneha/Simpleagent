import re


class RouterAgent:

    def route(self, request):

        request = request.lower().strip()

        # File extensions always mean code generation
        extensions = (
            ".py",
            ".java",
            ".c",
            ".cpp",
            ".js",
            ".html",
            ".css",
            ".sql"
        )

        if any(ext in request for ext in extensions):
            return "coding"

        # Coding action words
        coding_keywords = [
            "create",
            "generate",
            "write",
            "build",
            "develop",
            "implement",
            "code",
            "script",
            "function",
            "class",
            "algorithm"
        ]

        # Match whole words only
        words = re.findall(r"\b\w+\b", request)

        if any(keyword in words for keyword in coding_keywords):
            return "coding"

        return "theory"