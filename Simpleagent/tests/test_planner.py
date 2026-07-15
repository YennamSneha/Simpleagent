from agents.planner_agent import PlannerAgent


planner = PlannerAgent()


task = """
Plan a day of a busy senior software engineer
"""


steps = planner.plan(task)


print("Plan:")
print(steps)