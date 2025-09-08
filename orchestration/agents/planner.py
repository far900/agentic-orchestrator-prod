from orchestration.state import AgentState

def planner_tool(query: str) -> str:
    return "summarizer" if "summarize" in query.lower() else "search"

def planner_node(state: AgentState) -> AgentState:
    query = state.get("query", "")
    route = planner_tool(query)
    return {"route": route}
