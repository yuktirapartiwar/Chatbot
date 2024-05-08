
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI() #To import API Key from .env file


def main(message, model, role, temperature, max_tokens, tone):
    prompt = f"{message}\n{tone}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role":role, "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    
    return response.choices[0].message.content