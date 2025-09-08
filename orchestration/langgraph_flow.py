from typing import TypedDict
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph

from orchestration.agents.planner import planner_node
from orchestration.agents.executor import executor_node
from orchestration.state import AgentState

# Define the orchestration graph
graph = StateGraph(AgentState)
graph.add_node("Planner", RunnableLambda(planner_node))
graph.add_node("Executor", RunnableLambda(executor_node))
graph.set_entry_point("Planner")
graph.add_edge("Planner", "Executor")
graph.set_finish_point("Executor")

# Compile the graph
app = graph.compile()

# Optional: run directly for testing
if __name__ == "__main__":
    query = "summarize the latest GenAI trends in fintech"
    initial_state = {"query": query}
    response = app.invoke(initial_state)
    print(" Agentic Output:", response)