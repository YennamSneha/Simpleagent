from agents.approval_agent import ApprovalAgent


approval = ApprovalAgent()


code = """
print("Hello AI Agent")
"""


result = approval.approve(code)


print("Approved:", result)