# main.py

import json
from pathlib import Path

from src.graph import graph

from datetime import datetime


# ============================================================
# OUTPUT DIRECTORY
# ============================================================

# Create an "output" directory in the project root.
#
# Example:
#
# LangGraph-Software-Dev-Agent/
# ├── main.py
# └── output/
#
OUTPUT_DIR = Path("output")

# Create the directory if it does not already exist.
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================
# SAVE Response RESULT
# ============================================================

def save_response_file(response: str):

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    response_file = OUTPUT_DIR / f"final_response_{timestamp}.json"

    with open(response_file, "a", encoding="utf-8") as file:
        file.write(response)

    return response_file


# ============================================================
# SAVE COMPLETE EXECUTION RESULT
# ============================================================

def save_execution_result(result: dict):
    """
    Save the complete LangGraph state as JSON.

    This gives us an audit/debug file containing:
    """

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = OUTPUT_DIR / f"execution_result_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    return output_file

def run():

    print("\n===================================")
    print("      AI SUPPORT DEPARTMENT")
    print("===================================")

    print(
        "\nEnter a user issue."
    )

    print(
        "Type 'exit' to stop the application."
    )


    # --------------------------------------------------------
    # CONTINUOUS USER INPUT
    # --------------------------------------------------------

    while True:

        query = input(
            "\nEnter the issue: "
        )


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if query.lower().strip() == "exit":

            print("\nExiting application...")

            break


        # ----------------------------------------------------
        # INITIAL LANGGRAPH STATE
        # ----------------------------------------------------

        initial_state = {
            "customer_query": query,
            "category": "",
            "priority": "",
            "issue_summary": "",
            "generated_response": "",
            "review_feedback": "",
            "approved": False,
            "iteration_count": 0
        }

        # ----------------------------------------------------
        # RUN LANGGRAPH
        # ----------------------------------------------------

        result = graph.invoke(
            initial_state
        )

        #-----------------------------------------------------
        # FINAL RESPONSE
        #-----------------------------------------------------

        print(f"\n RESPONSE: {result["generated_response"]}")

        response_file = save_response_file(result["generated_response"])

        # ====================================================
        # SAVE COMPLETE RESULT
        # ====================================================

        result_file = save_execution_result(result)

        # ====================================================
        # PRINT EXECUTION SUMMARY
        # ====================================================

        print("\n")
        print("===================================")
        print("        EXECUTION SUMMARY")
        print("===================================")

        print(f"Execution File: {result_file} Response file: {response_file}")

        print(f"\n \n {result}")


# ============================================================
# PYTHON ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run()