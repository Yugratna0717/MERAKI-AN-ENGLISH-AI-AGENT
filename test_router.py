from agents.router import router_agent

queries = [
    "Correct this sentence: He don't like apples.",
    "What is the meaning of meticulous?",
    "Write a formal leave application.",
    "Explain the theme of Macbeth."
]

for q in queries:
    print("Question:", q)
    print("Route:", router_agent(q))
    print("-" * 40)