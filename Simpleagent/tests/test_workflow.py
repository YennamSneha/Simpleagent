from workflows.workflow import CodingWorkflow


agent = CodingWorkflow()


request = """
Create a Python program to add two numbers
and print the result.
"""


result = agent.run(request)


print(result)