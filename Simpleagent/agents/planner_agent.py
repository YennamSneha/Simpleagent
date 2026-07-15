from llm.ollama_client import LLMClient


class PlannerAgent:

    def plan(self, task):

        system_prompt = """
You are a project planner.

Break the coding task into a maximum of 5 clear steps.

Return only the numbered steps.

Keep the answer concise.
"""

        return LLMClient.generate(
            system_prompt,
            task
        )