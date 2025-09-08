from orchestration.state import AgentState

def executor_node(state: AgentState) -> AgentState:
    route = state.get("route")
    query = state.get("query", "")

    if route == "summarizer":
        result = f"[SUMMARY] {query[:80]}..."
    else:
        result = f"[SEARCH] Results for: {query}"

    return {"result": result}
