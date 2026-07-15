from agents.memory_agent import MemoryAgent


memory = MemoryAgent()


memory.save(
    "Create calculator",
    "Created calculator.py"
)


result = memory.get_memory()


print(result)