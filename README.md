## Objective

Build an **AI-powered Customer Support Resolution Agent using LangGraph**.
The application should receive a customer question or complaint and use multiple specialized AI steps to:
    
    1. Understand the customer issue. 
    
    2. Classify the issue. 
    
    3. Draft a response. 
    
    4. Review the response. 
    
    5. Decide whether the response needs improvement. 
    
    6. Improve it if necessary. 
    
    7. Produce the final response. 
    
The goal is **to demonstrate your understanding of LangGraph-based agentic workflows**, rather than simply building a chatbot.

## Workflow

```
                         CUSTOMER QUERY
                                │
                                ▼
                     ┌────────────────────┐
                     │   UNDERSTAND NODE  │
                     │                    │
                     │ Understand issue   │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │  CLASSIFY NODE     │
                     │                    │
                     │ Category           │
                     │ Priority           │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │ RESPONSE NODE      │
                     │                    │
                     │ Draft response     │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │  REVIEW NODE       │
                     │                    │
                     │ Review response    │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │     ROUTER         │
                     │                    │
                     │ Good response?     │
                     └──────┬───────┬─────┘
                            │       │
                         NO │       │ YES
                            │       │
                            ▼       ▼
                      ┌────────┐ ┌──────────┐
                      │  FIX   │ │  FINAL   │
                      │        │ │ RESPONSE │
                      └────┬───┘ └────┬─────┘
                           │          │
                           ▼          ▼
                        REVIEW       END
```

## File Structure

```
customer-support/
├── .env.example              # Environment variable template
├── .gitignore                # Git ignore file
├── pyproject.toml            # Dependencies and build system configuration
├── uv.lock                   # Lockfile for reproducible installs
├── README.md                 # Project documentation
│
├── app/
│   ├── __init__.py           # Package initialization
│   ├── state.py              # TypedDict state definition
│   ├── prompts.py            # Node system prompts
│   ├── nodes.py              # LangGraph node functions & structured outputs
│   └── graph.py              # StateGraph definition and conditional routing
│
├── output/                   # Directory created dynamically at runtime
│   ├── final_response.txt    # Text output of final draft
│   └── execution_result.json # Complete state trace log
│
└── main.py                   # CLI entry point

```

## How to run
uv pip install -r requirements.txt

uv run python main.py

## ENV file sample:
GROQ_API_KEY="your-groq-api-key-here"

