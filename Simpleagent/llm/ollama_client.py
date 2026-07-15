from ollama import Client
from config import MODEL, TEMPERATURE, KEEP_ALIVE

client = Client(host="http://localhost:11434")

conversation_history = []
MAX_HISTORY = 6


class LLMClient:

    @staticmethod
    def generate(system_prompt, user_prompt):

        global conversation_history

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(conversation_history)

        messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        response = client.chat(
            model=MODEL,
            messages=messages,
            options={
                "temperature": TEMPERATURE
            },
            keep_alive=KEEP_ALIVE
        )

        answer = response["message"]["content"]

        conversation_history.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        conversation_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        if len(conversation_history) > MAX_HISTORY:
            conversation_history = conversation_history[-MAX_HISTORY:]

        return answer