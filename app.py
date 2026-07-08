from flask import Flask, render_template, request, jsonify

from graph.graph_builder import graph

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get JSON data from frontend
        data = request.get_json()

        # Extract user message
        user_input = data.get("message", "").strip()

        # Validate input
        if not user_input:
            return jsonify({
                "error": "Message cannot be empty."
            }), 400

        # Invoke LangGraph
        result = graph.invoke({
            "user_input": user_input
        })

        # Send response back to frontend
        return jsonify({
            "agent": result["agent"].capitalize(),
            "response": result["output"]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )