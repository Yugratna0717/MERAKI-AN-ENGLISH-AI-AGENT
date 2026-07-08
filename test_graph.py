from graph.graph_builder import graph


queries = [
    "Correct this sentence: He don't likes cricket.",
    "What is the meaning of meticulous?",
    "Explain the theme of Macbeth.",
    "Write a formal leave application."
]


for query in queries:
    print("=" * 60)
    print("USER:", query)

    result = graph.invoke(
        {
            "user_input": query
        }
    )

    print("\nSelected Agent:", result["agent"])
    print("\nResponse:\n")
    print(result["output"])
    print("=" * 60)
    print()