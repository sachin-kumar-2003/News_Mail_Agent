import os
import json
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from system_prompt import system_prompt
api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

user_query = "i want latest sports news"
messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user", 
            "content": user_query
        },
        {
            "role":"user",
            "content":"{'step': 'plan', 'content': 'The user is interested in the latest sports news.'}"
        }
    ]

response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=messages,
        )
print(response)
raw = response.choices[0].message.content
print(raw)