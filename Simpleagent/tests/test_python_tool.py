from tools.runner import run_python_file


result = run_python_file(
    "generated_files/detail.py"
)

print("Output:")
print(result)