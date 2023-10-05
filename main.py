import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def query_chatgpt(prompt, api_key=os.getenv('OPENAI_API_KEY')):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'model': 'gpt-3.5-turbo',  # specify the model to use
        'messages': [
            {'role': 'system', 'content': 'You are an ia in a robot named Edog. Your responses will be sharp and short, never anwser with more than 100 words'},
            {'role': 'user', 'content': prompt},
        ]
    }

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 200:
        model_response = response.json()['choices'][0]['message']['content']
        return model_response
    else:
        raise ConnectionError("API request failed", response.text)

if __name__ == '__main__':
    prompt = input("What would you like to ask GPT-4? ")
    try:
        response = query_chatgpt(prompt)
        print("GPT-4 says:", response)
    except ConnectionError as e:
        print(e)
