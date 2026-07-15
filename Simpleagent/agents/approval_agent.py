class ApprovalAgent:


    def approve(self, code):

        print("\nGenerated Code:")
        print("----------------")
        print(code)
        print("----------------")


        choice = input(
            "\nApprove this code? (yes/no): "
        )


        if choice.lower() == "yes":
            return True

        return False