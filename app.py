from flask import Flask, render_template, request
from chatbot import main as chat_message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        temperature = float(request.form['temperature'])
        max_tokens = int(request.form['max_tokens'])
        tone = request.form['tone']
        model = "gpt-3.5-turbo"
        conversation_history = chat_message(message, model, temperature, max_tokens, tone)
    return render_template('index.html', conversation_history=conversation_history)

if __name__ == '__main__':
    app.run(debug=True)