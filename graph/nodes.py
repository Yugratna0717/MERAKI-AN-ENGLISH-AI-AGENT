from agents.router import router_agent
from agents.grammar_agent import grammar_agent
from agents.vocabulary_agent import vocabulary_agent
from agents.literature_agent import literature_agent
from agents.writing_agent import writing_agent


def router_node(state):
    """
    Determines which agent should handle the request.
    """

    user_input = state["user_input"]

    selected_agent = router_agent(user_input)

    return {
        "agent": selected_agent
    }


def grammar_node(state):
    """
    Executes the Grammar Agent.
    """

    result = grammar_agent(state["user_input"])

    return {
        "output": result
    }


def vocabulary_node(state):
    """
    Executes the Vocabulary Agent.
    """

    result = vocabulary_agent(state["user_input"])

    return {
        "output": result
    }


def literature_node(state):
    """
    Executes the Literature Agent.
    """

    result = literature_agent(state["user_input"])

    return {
        "output": result
    }


def writing_node(state):
    """
    Executes the Writing Agent.
    """

    result = writing_agent(state["user_input"])

    return {
        "output": result
    }