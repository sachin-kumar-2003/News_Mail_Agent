import os
import json
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from news import national_news, international_news, sports_news, technology_news
from system_prompt import system_prompt
from check_json import fixed_json
from send_mail import send_mail_reciever

class NewRequest(BaseModel):
    usermail: str
    userquery: str

# for mail section
subject = ""


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to the News Mail Agent Backend!"}

@app.post("/news")
async def news(data: NewRequest):
    api_key = os.getenv("GEMINI_API_KEY")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    user_mail = data.usermail
    user_query = data.userquery
    
    tools = {
        "national_news": national_news,
        "international_news": international_news,
        "sports_news": sports_news,
        "technology_news": technology_news
    }
    
    
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


    while True:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=messages,
        )
        print(response)
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
            subject = fn_name
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
            res = send_mail_reciever(subject = subject, allnews=res["content"], receivermail = user_mail)
            if res:
                return {"response": "Mail sent succesfully ... "}
            else:
                return {"response": "Something went Wrong"}
            break

