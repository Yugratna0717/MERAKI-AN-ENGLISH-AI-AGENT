from services.gemini import llm

response = llm.invoke("Introduce yourself in one sentence.")

print(response.content)