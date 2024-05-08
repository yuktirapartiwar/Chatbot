
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI() #To import API Key from .env file

conversation_history = []

def main(message, model, temperature, max_tokens, tone):
    global conversation_history

    prompt = f"{message}\n{tone}"

    conversation_history.append({"role": 'user', "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=conversation_history,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    bot_response = response.choices[0].message.content

    conversation_history.append({"role": 'assistant', "content": bot_response})
    
    return conversation_history