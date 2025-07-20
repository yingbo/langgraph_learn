import os
import sys
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import random



class State(TypedDict):
    description: str


def node_1(state: State) -> State:
    print("Node 1")
    return {"description": "Node 1"}

def node_2(state: State) -> State:
    print("Node 2")
    return {"description": "Node 2"}


def node_3(state: State) -> State:
    print("Node 3")
    return {"description": "Node 2"}


def decide_mood(state: State) -> str:
    print("Decide mood")
    a = random.randint(0, 100)
    print(f"Random number: {a}")
    if a < 50:
        return "node_2"
    return "node_3"

def main():
    builder = StateGraph(State)

    builder.add_node("node_1", node_1)
    builder.add_node("node_2", node_2)
    builder.add_node("node_3", node_3)

    builder.add_edge(START, "node_1")
    builder.add_conditional_edges("node_1", decide_mood)    
    builder.add_edge("node_2", END)
    builder.add_edge("node_3", END)
    
    graph = builder.compile()
    
    a = graph.get_graph().draw_mermaid_png()
    print("Graph structure saved as PNG.")

    # Save PNG data to a file
    png_path = "graph.png"
    with open(png_path, "wb") as f:
        f.write(a)

    # Open the PNG file using the default viewer (Mac)
    os.system(f"open {png_path}")
    
    graph.invoke({"description": "Start state"})
if __name__ == "__main__":
    main()
