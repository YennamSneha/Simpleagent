from agents.coder_agent import CoderAgent


coder = CoderAgent()


task = """
Create a Python program for the task loops
"""


code = coder.generate_code(task)


print("Generated Code:")
print(code)