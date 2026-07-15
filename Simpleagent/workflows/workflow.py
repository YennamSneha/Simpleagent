import time

from agents.planner_agent import PlannerAgent
from agents.reviewer_agent import ReviewerAgent
from agents.approval_agent import ApprovalAgent
from agents.coder_agent import CoderAgent
from agents.memory_agent import MemoryAgent

from tools.language_detector import detect_filename
from tools.file_tool import create_file
from tools.runner import run_file
from tools.code_extractor import extract_code


class CodingWorkflow:

    def __init__(self):

        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.approval = ApprovalAgent()
        self.memory = MemoryAgent()

    def run(self, request):

        total_start = time.time()

        # ---------------- PLAN ----------------

        print("\nPlanning...\n")

        plan = self.planner.plan(request)

        print(plan)

        # ---------------- GENERATE CODE ----------------

        print("\nGenerating code...\n")

        start = time.time()

        code = self.coder.generate_code(
            f"""
Task:
{request}

Plan:
{plan}
"""
        )

        code = extract_code(code)

        print(f"✅ Code generated in {time.time() - start:.2f} sec")

        # ---------------- REVIEW ----------------

        print("\nReviewing code...\n")

        review = self.reviewer.review(code)

        print(review)

        # ---------------- APPROVAL ----------------

        approved = self.approval.approve(code)

        if not approved:

            print("\nCode rejected.")

            return

        # ---------------- FILE NAME ----------------

        filename = detect_filename(request)

        # ---------------- CREATE FILE ----------------

        print("\nCreating file...\n")

        create_file(filename, code)

        print(f"✅ File created : {filename}")

        # ---------------- RUN PROGRAM ----------------

        print("\nRunning program...\n")

        start = time.time()

        result = run_file(
            "generated_files/" + filename
        )

        print(f"✅ Execution completed in {time.time() - start:.2f} sec")

        # ---------------- SUCCESS ----------------

        if result["success"]:

            print("\n========== OUTPUT ==========\n")

            print(result["output"])

        # ---------------- FAILURE ----------------

        else:

            print("\nProgram failed.")

            print(result["error"])

            print("\nTrying one automatic fix...\n")

            start = time.time()

            fixed_code = self.coder.fix_code(
                code,
                result["error"]
            )

            fixed_code = extract_code(fixed_code)

            print(f"✅ Fix generated in {time.time() - start:.2f} sec")

            print("\nCreating fixed file...\n")

            create_file(
                filename,
                fixed_code
            )

            print("\nRunning fixed program...\n")

            result = run_file(
                "generated_files/" + filename
            )

            if result["success"]:

                print("\n========== FIXED OUTPUT ==========\n")

                print(result["output"])

            else:

                print("\nStill failing.\n")

                print(result["error"])

        # ---------------- MEMORY ----------------

        self.memory.save(
            request,
            "Completed : " + filename
        )

        print(
            f"\n🎉 Total Time : {time.time() - total_start:.2f} sec\n"
        )