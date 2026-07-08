from langchain_core.prompts import ChatPromptTemplate

from services.gemini import llm
from prompts.grammar_prompt import SYSTEM_PROMPT


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{user_input}")
    ]
)

grammar_chain = prompt | llm


def grammar_agent(user_input: str) -> str:
    """
    Processes the user's input using the Grammar Agent.

    Args:
        user_input (str): The sentence or grammar question.

    Returns:
        str: The AI-generated grammar correction and explanation.
    """

    response = grammar_chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content