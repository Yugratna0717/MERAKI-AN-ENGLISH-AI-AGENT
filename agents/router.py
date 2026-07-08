from langchain_core.prompts import ChatPromptTemplate

from services.gemini import llm
from prompts.router_prompt import SYSTEM_PROMPT


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{user_input}")
    ]
)

router_chain = prompt | llm


def router_agent(user_input: str) -> str:
    """
    Determines which agent should handle the user's request.

    Returns:
        grammar
        vocabulary
        literature
        writing
    """

    response = router_chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content.strip().lower()