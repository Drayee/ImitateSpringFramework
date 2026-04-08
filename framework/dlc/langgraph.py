"""
    langgraph
    基于 langgraph 实现的 langchain 应用
"""

from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class Main(BaseMain):
    def __init__(self):

        class State(TypedDict):
            messages: Annotated[Sequence[BaseMessage], add_messages]

        self.workflow = StateGraph(State)
        library.dependency["langgraph"] = {}

    def build(self):
        for name, func in library.dependency["langgraph"].items():
            self.workflow.add_node(name, func)

        library.resource["langgraph_app"] = self.workflow.compile()

def langgraph_node(name = None):
    def decorator(func):
        nonlocal name
        if name is None:
            name = func.__name__
        library.dependency["langgraph"][name] = func
        return func
    return decorator