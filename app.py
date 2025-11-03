from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "name" in user_input:
        return "I'm your cloud chatbot made with Python!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm still learning. Can you rephrase that?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
