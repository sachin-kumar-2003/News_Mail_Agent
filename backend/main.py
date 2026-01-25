import os
import json
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from news import national_news, international_news, sports_news, technology_news
from system_prompt import system_prompt


api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = {
    "national_news": {
        "function": national_news,
        "description": "Fetches the latest national news headlines."
    },
    "international_news": {
        "function": international_news,
        "description": "Fetches the latest international news headlines."
    },
    "sports_news": {
        "function": sports_news,
        "description": "Fetches the latest sports news headlines."
    },
    "technology_news": {
        "function": technology_news,
        "description": "Fetches the latest technology news headlines."
    }
}

messages = [
    {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user", 
            "content": input("enter your query >> ")
        }
]


while True:
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=messages,
    )

    assistant_content = response.choices[0].message.content

    parsed_response = json.loads(assistant_content)
    print(parsed_response)
    step = parsed_response["step"]
    
    messages.append({
        "role": "assistant",
        "content": json.dumps(parsed_response)
    })

    print("Assistant Response:", assistant_content)

    if step == "plan":
        print("Planning:", parsed_response.get("content"))
    elif step == "action":
        function_name = parsed_response.get("function")
        if not function_name or function_name not in tools:
            print("Error: Invalid function name.")
            break
        all_news = tools[function_name]["function"]()
        messages.append({"role":"user", "content": f"make a concise summary of all_news : {all_news}"})
    elif step == "observe":
        observation = parsed_response.get("content")
        print("Observation:", observation)
        messages.append({"role":"user", "content": f"Observation: {observation}"})
        break




app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the News Mail Agent Backend!"}

