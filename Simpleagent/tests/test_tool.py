from tools.file_tool import create_file

result = create_file(
    "hello.py",
    "print('Hello from agent')"
)

print(result)