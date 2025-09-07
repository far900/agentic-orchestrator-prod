from langgraph.graph import StateGraph
from tools.search_tool import search_tool
from agents.planner import planner_agent
from agents.executor import executor_agent

graph = StateGraph()
graph.add_node("Planner", planner_agent)
graph.add_node("Executor", executor_agent)
graph.add_edge("Planner", "Executor")
graph.add_tool("Search", search_tool)
graph.set_entry_point("Planner")
graph.compile().run()
