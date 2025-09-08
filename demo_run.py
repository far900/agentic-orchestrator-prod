from orchestration.langgraph_flow import app

query = "summarize the latest GenAI trends in fintech"
initial_state = {"query": query}

response = app.invoke(initial_state)
print(" Agentic Output:", response)