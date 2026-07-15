import json
import os


class MemoryAgent:

    def __init__(self):

        self.file = "memory/conversations.json"


        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)



    def save(self, user, assistant):

        with open(self.file, "r") as f:
            data = json.load(f)


        data.append(
            {
                "user": user,
                "assistant": assistant
            }
        )


        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


        return "Memory saved"



    def get_memory(self):

        with open(self.file, "r") as f:
            data = json.load(f)


        return data