import os


def search_knowledge(query):

    results = []

    folder = "knowledge_base"


    for file in os.listdir(folder):

        path = os.path.join(folder, file)


        with open(path, "r") as f:

            content = f.read()


            if any(
                word.lower() in content.lower()
                for word in query.split()
            ):
                results.append(content)


    return results