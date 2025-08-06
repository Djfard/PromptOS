import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

TestInput = "I want a meal plan for gym"

response = client.chat.completions.create(
    model="gpt-4.1-mini", 
    messages=[
        {
            "role": "system",
            "content": "You are an expert prompt engineer. You are tasked to enhance the user's prompt using methods from recent prompt research."
        },
        {
            "role": "user",
            "content": TestInput
        }
    ]
)

print(response.choices[0].message.content)
