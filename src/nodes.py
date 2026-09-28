import os
import json

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from src.prompts import UNDERSTAND_PROMPT, CLASSIFY_PROMPT, RESPONSE_PROMPT, REVIEW_PROMPT, FIX_PROMPT
from src.state import AgentState

from logger import logging

## Step 1: load env variables
load_dotenv()

## Step 2: Create the llm
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ API KEY is missing. Please add it to your .env file")

## Step 3: Create chatGroq model
llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0.2,
    api_key=groq_api_key
)


## Helper function
def invoke_llm(prompt: str) -> str:
    """
    Send a prompt to the llm and return plain text. this is done because our state stores only strings
    """
    response = llm.invoke(prompt)
    return response.content

# Understand Node:
def understand_node(state: AgentState) -> dict:
    logging.info("INSIDE UNDERSTAND NODE")

    prompt = UNDERSTAND_PROMPT.format(
        query = state["customer_query"]
    )

    issue_summary = invoke_llm(prompt)

    logging.info("QUERY UNDERSTOOD SUCCESSFULLY")

    return {
        "issue_summary": issue_summary
    }

# Classify Node:
def classify_node(state: AgentState) -> dict:
    logging.info("INSIDE CLASSIFY NODE")
    
    prompt = CLASSIFY_PROMPT.format(
        summary = state["issue_summary"]
    )
    
    response = invoke_llm(prompt)
    result = json.loads(response)
    
    logging.info("QUERY CLASSIFY SUCCESSFULLY")
    
    return {
        "category": result["category"],
        "priority": result["priority"]
    }

# Response Node
def response_node(state: AgentState) -> dict:
    logging.info("INSIDE RESPONSE NODE")
    
    prompt = RESPONSE_PROMPT.format(
        summary = state["issue_summary"],
        category = state["category"],
        priority = state["priority"]
    )
    
    response = invoke_llm(prompt)

    logging.info("QUERY RESPONSE SUCCESSFULLY")
    
    return {
        "generated_response": response
    }  

# Review Node
def review_node(state: AgentState) -> dict:
    logging.info("INSIDE REVIEW NODE")
    
    prompt = REVIEW_PROMPT.format(
        summary = state["issue_summary"],
        category = state["category"],
        priority = state["priority"],
        draft_response = state["generated_response"]
    )
    
    response = invoke_llm(prompt)
    result = json.loads(response)

    logging.info("RESPONSE REVIEWED SUCCESSFULLY")
    
    return {
        "review_feedback": result["feedback"],
        "approved": result["approved"]
    }

## FIX Node
def fix_node(state: AgentState)-> dict:
    logging.info("INSIDE FIX NODE")

    prompt = FIX_PROMPT.format(
        original_message = state["customer_query"],
        category = state["category"],
        priority = state["priority"],
        draft_response = state["generated_response"],
        review_feedback = state["review_feedback"]
    )

    improved_response = invoke_llm(prompt)

    new_iteration_count = (state["iteration_count"]+ 1)

    logging.info("FIX NODE: RESPONSE IMPROVED SUCCESSFULLY")
    logging.info(f"Current iteration: {new_iteration_count}" )

    return {
        "generated_response": improved_response, 
        "iteration_count": new_iteration_count
    }