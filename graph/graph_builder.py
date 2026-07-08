from langgraph.graph import StateGraph, START, END

from graph.state import GraphState
from graph.nodes import (
    router_node,
    grammar_node,
    vocabulary_node,
    literature_node,
    writing_node,
)


# Create the graph
builder = StateGraph(GraphState)


# Add nodes
builder.add_node("router", router_node)
builder.add_node("grammar", grammar_node)
builder.add_node("vocabulary", vocabulary_node)
builder.add_node("literature", literature_node)
builder.add_node("writing", writing_node)


# Start -> Router
builder.add_edge(START, "router")


# Function to decide the next node
def route(state):
    return state["agent"]


# Conditional Routing
builder.add_conditional_edges(
    "router",
    route,
    {
        "grammar": "grammar",
        "vocabulary": "vocabulary",
        "literature": "literature",
        "writing": "writing",
    },
)


# Agent -> END
builder.add_edge("grammar", END)
builder.add_edge("vocabulary", END)
builder.add_edge("literature", END)
builder.add_edge("writing", END)


# Compile the graph
graph = builder.compile()