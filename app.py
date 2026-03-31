from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hello 👋",
        "hi": "Hi there 😊",
        "how are you": "I'm fine 😄 What about you?",
        "your name": "I am your chatbot 🤖",
        "bye": "Goodbye 👋",
        "help": "You can ask me basic questions!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Hmm 🤔 I don't understand. Try something else!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = chatbot_response(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
