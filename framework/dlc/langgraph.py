"""
    langgraph
    基于 langgraph 实现的 langchain 应用
"""

from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

logger = logging.getLogger(__name__)

class Main(BaseMain):
    def __init__(self):

        self.app = None

        # 定义状态
        class State(TypedDict):
            messages: Annotated[Sequence[BaseMessage], add_messages]

        self.workflow = StateGraph(State)
        library.dependency["langgraph"] = {}

    def build(self):
        for name, func in library.dependency["langgraph"].items():
            self.workflow.add_node(name, func)

        self.app = self.workflow.compile()

        # 定义获取 langgraph 图的函数
        def get_graph():
            try:
                from IPython.display import display, Image
                display(Image(self.app.get_graph(xray=True).draw_png()))
            except Exception as e:
                logger.error(f"获取 langgraph 图失败: {e}")

        library.resource["get_graph"] = get_graph

        library.resource["langgraph_app"] = self.app

def langgraph_node(name = None):
    def decorator(func):
        nonlocal name
        if name is None:
            name = func.__name__
        library.dependency["langgraph"][name] = func
        return func
    return decorator