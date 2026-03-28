from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "What is the FizzBuzz problem?"}
    ]
)

print("=== LAB 2.1 ===")
print(completion.choices[0].message.content)