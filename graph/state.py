from typing_extensions import TypedDict


class GraphState(TypedDict):
    user_input: str
    agent: str
    output: str