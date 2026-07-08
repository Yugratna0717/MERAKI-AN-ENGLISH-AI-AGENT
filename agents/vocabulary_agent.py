from langchain_core.prompts import ChatPromptTemplate

from services.gemini import llm
from prompts.vocabulary_prompt import SYSTEM_PROMPT


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{user_input}")
    ]
)

vocabulary_chain = prompt | llm


def vocabulary_agent(user_input: str) -> str:
    """
    Processes vocabulary-related queries.

    Args:
        user_input (str): The user's vocabulary question.

    Returns:
        str: AI-generated vocabulary response.
    """

    response = vocabulary_chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content