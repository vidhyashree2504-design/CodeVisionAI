from flask import Flask, request, jsonify
from flask_cors import CORS
from refactor import refactor_code
from bot import get_bot_response

# CREATE THE APP FIRST
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Automated Code Refactoring Tool Backend is Running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    code = data.get("code")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    refactored_code, suggestions = refactor_code(code)

    explanation = []

    if "+=" in refactored_code:
        explanation.append("Replaced traditional addition with shorthand operator")

    explanation.append("Improved code readability")
    explanation.append("Applied clean coding practices")

    return jsonify({
        "original_code": code,
        "refactored_code": refactored_code,
        "suggestions": suggestions,
        "explanation": explanation
    })


# ADD THIS NEW CHAT ROUTE
@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_message = data.get("message")

    bot_reply = get_bot_response(user_message)

    return jsonify({
        "reply": bot_reply
    })

# RUN APP AT THE END
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
