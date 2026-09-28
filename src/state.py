
from typing_extensions import TypedDict

class AgentState(TypedDict):
    customer_query: str
    category: str
    priority: str
    issue_summary: str
    generated_response: str
    review_feedback: str
    approved: bool
    iteration_count: int
