from langchain_core.prompts import ChatPromptTemplate

from services.gemini import llm
from prompts.writing_prompt import SYSTEM_PROMPT


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{user_input}")
    ]
)

writing_chain = prompt | llm


def writing_agent(user_input: str) -> str:
    """
    Processes writing-related requests.

    Args:
        user_input (str): The user's writing request.

    Returns:
        str: AI-generated writing response.
    """

    response = writing_chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content