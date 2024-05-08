from flask import Flask, render_template, request
from chatbot import main as chat_message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    bot_response = None
    if request.method == 'POST':
        message = request.form['message']
        temperature = float(request.form['temperature'])
        max_tokens = int(request.form['max_tokens'])
        tone = request.form['tone']
        model = "gpt-3.5-turbo"
        role = "user"
        bot_response = chat_message(message, model, role, temperature, max_tokens, tone)
    return render_template('index.html', bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)