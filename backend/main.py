import os
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from news import national_news, international_news, sports_news, technology_news



api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools =[
    {
        "name":"national_news",
        "function": national_news,
        "description":"Fetches the latest national news articles."
    },
    {
        "name":"international_news",
        "function": international_news,
        "description":"Fetches the latest international news articles."
    },
    {
        "name":"sports_news",
        "function": sports_news,
        "description":"Fetches the latest sports news articles."
    },
    {
        "name":"technology_news",
        "function": technology_news,
        "description":"Fetches the latest technology news articles."
    }
]


# response = client.chat.completions.create(
#     model="gemini-3-flash-preview",
#     messages=[
#         {
#             "role":"user",
#             "content":"hey"
#         }
#     ]
# )
# print(response.choices[0].message.content)




app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the News Mail Agent Backend!"}

