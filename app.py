from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello 👋"
    elif "how are you" in user_input:
        return "I'm fine! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye 😊"
    else:
        return "Sorry, I didn't understand."

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
