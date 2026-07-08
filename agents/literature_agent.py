from langchain_core.prompts import ChatPromptTemplate

from services.gemini import llm
from prompts.literature_prompt import SYSTEM_PROMPT


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{user_input}")
    ]
)

literature_chain = prompt | llm


def literature_agent(user_input: str) -> str:
    """
    Processes literature-related questions.

    Args:
        user_input (str): The user's literature question.

    Returns:
        str: AI-generated literature response.
    """

    response = literature_chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content