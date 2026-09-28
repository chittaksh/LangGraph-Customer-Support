from langgraph.graph import StateGraph, END
from src.state import AgentState

from src.nodes import (understand_node, classify_node, response_node, review_node, fix_node)
from logger import logging

## Step 1: Create graph builder
workflow = StateGraph(AgentState)

## Step 2: Register nodes
workflow.add_node("understand", understand_node)
workflow.add_node("classify", classify_node)
workflow.add_node("response", response_node)
workflow.add_node("review", review_node)
workflow.add_node("fix", fix_node)

## Step 3: Define the sequence of the nodes
workflow.set_entry_point("understand")

workflow.add_edge("understand", "classify")
workflow.add_edge("classify", "response")
workflow.add_edge("response", "review")

def review_router(state: AgentState) -> dict:
    logging.info(f"Approved: {bool(state["approved"])}")
    logging.info(f"Iteration count: {state["iteration_count"]}")

    if (bool(state["approved"]) == False and state["iteration_count"] < 1):
        logging.info("Routing to FIX")
        return "fix"
    logging.info("Routing to END")
    return END

workflow.add_edge("fix", "review")

workflow.add_conditional_edges("review", review_router)

## Step 4: Compile Graph
graph = workflow.compile()