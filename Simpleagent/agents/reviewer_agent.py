from ollama import chat


class ReviewerAgent:

    def review(self, code):

        response = chat(
            model="qwen2.5-coder",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a code reviewer.

Rules:
- Review ONLY the given source code.
- Never refuse.
- Never answer general questions.
- Never apologize.
- Return only review points.
"""
                },
                {
                    "role": "user",
                    "content": code
                }
            ]
        )

        return response["message"]["content"]