import os


def search(query):

    results = []

    folder = "knowledge_base"

    if not os.path.exists(folder):
        return []

    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        if os.path.isfile(path):

            with open(path, "r", encoding="utf-8") as file:

                text = file.read()

                if query.lower() in text.lower():

                    results.append(
                        {
                            "file": filename,
                            "content": text
                        }
                    )

    return results