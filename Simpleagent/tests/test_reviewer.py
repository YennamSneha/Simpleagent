from agents.reviewer_agent import ReviewerAgent


reviewer = ReviewerAgent()


code = """
def add(a,b)
    return a+b
"""


result = reviewer.review(code)

print(result)