import os
import json
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from news import national_news, international_news, sports_news, technology_news
from system_prompt import system_prompt
from check_json import fixed_json


api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)
tools = {
        "national_news": national_news,
        "international_news": international_news,
        "sports_news": sports_news,
        "technology_news": technology_news
    }

user_query = input("enter your query = ")
messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user", 
            "content": user_query
        },
]


# print(technology_news())
while True:
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=messages,
    )

    raw = response.choices[0].message.content

    if not raw or raw.strip() == "":
        print("Empty model response — stopping.")
        break

    res = fixed_json(raw)
    print("parsed:", res)

    messages.append({"role": "assistant", "content": raw})

    step = res.get("step")

    if step == "plan":
        messages.append({
            "role": "user",
            "content": "Continue to the next step."
        })
        continue

    if step == "action":
        fn_name = res["function"]
        fn = tools[fn_name]
        observation = fn()

        messages.append({
            "role": "user",
            "content": f"{observation} Provide the final answer output in more structure way"
        })
        continue

    if step == "observe":
        messages.append({
            "role": "user",
            "content": "Provide the final answer."
        })
        continue

    if step == "output":
        print("\nFINAL ANSWER:\n", res["content"])
        break

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the News Mail Agent Backend!"}