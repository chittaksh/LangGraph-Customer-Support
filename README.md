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
                     └────────┬─────┬─────┘
                              │     │
                         NO   │     │ YES
                              │     │
                              ▼     ▼
                         ┌────────┐ ┌──────────┐
                         │  FIX   │ │  FINAL   │
                         │        │ │ RESPONSE │
                         └────┬───┘ └────┬─────┘
                              │          │
                              ▼          ▼
                           REVIEW       END
```



