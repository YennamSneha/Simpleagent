from workflows.workflow import CodingWorkflow
from agents.router_agent import RouterAgent
from agents.theory_agent import TheoryAgent


def main():

    workflow = CodingWorkflow()
    router = RouterAgent()
    theory = TheoryAgent()


    print("=" * 50)
    print("AI Assistant Started")
    print("=" * 50)


    while True:

        request = input("\nYou: ")


        if request.lower() == "exit":
            break


        task_type = router.route(request)


        if task_type == "coding":

            workflow.run(request)


        else:

            answer = theory.answer(request)

            print("\nAgent:")
            print(answer)



if __name__ == "__main__":
    main()