from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  
  model="openai/gpt-5.2",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ],
  max_tokens=500,
)

print(completion.choices[0].message.content)
