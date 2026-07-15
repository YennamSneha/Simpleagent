from llm.ollama_client import LLMClient


class CoderAgent:

    def generate_code(self, request):

        system_prompt = """
You are an expert software engineer.

Generate source code in the programming language requested by the user.

Language Rules:
- .py  -> Python
- .java -> Java
- .c -> C
- .cpp -> C++
- .js -> JavaScript
- .html -> HTML
- .css -> CSS
- .sql -> SQL

Review Checklist (before returning):
- Verify the code is syntactically correct.
- Verify the code is complete.
- Verify all brackets are balanced.
- Verify all variables are declared.
- Verify all functions/classes are complete.
- Verify imports are included if required.
- Verify the code can compile or execute.
- Do not mix programming languages.
- Return the entire program.

Output Rules:
- Return ONLY source code.
- No explanations.
- No markdown.
- No ``` blocks.
- No headings.
- No English sentences.
- No expected output.
- No notes.
- No comments outside the code.
- No XML tags.
- No special characters outside the code.

Return only executable source code.
"""

        return LLMClient.generate(system_prompt, request)


    def fix_code(self, code, error):

        system_prompt = """
You are an expert software engineer and debugging agent.

Your task is to repair the given program.

Instructions:
- Detect the programming language automatically.
- Fix every syntax error.
- Fix every compilation error.
- Fix every runtime error.
- Preserve the original language.
- Preserve the program functionality.
- Add missing imports if required.
- Add missing semicolons if required.
- Add missing braces if required.
- Correct indentation.
- Complete incomplete functions.
- Complete incomplete classes.
- Remove invalid text.
- Remove explanations.
- Remove markdown.
- Remove code fences.
- Remove headings.
- Remove English sentences.

Before returning:
- Review the complete program.
- Verify the code is syntactically correct.
- Verify it can compile.
- Verify it can execute.

Output Rules:
- Return ONLY executable source code.
- No explanations.
- No markdown.
- No ``` blocks.
- No notes.
- No headings.
- No expected output.
- No English text.

Return only corrected source code.
"""

        prompt = f"""
Source Code:

{code}

Compiler/Runtime Error:

{error}
"""

        return LLMClient.generate(system_prompt, prompt)