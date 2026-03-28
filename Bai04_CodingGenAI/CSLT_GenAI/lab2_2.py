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
    temperature=0.2,
    max_tokens=100,
    n=1,
    messages=[
        {"role": "system", "content": "You are a hiring manager at a tech company."},
        {"role": "user", "content": "What is the Two Sum problem?"}
    ],
)

print("=== LAB 2.2 ===")
print("Completion Tokens:", completion.usage.completion_tokens)
print("Prompt Tokens:", completion.usage.prompt_tokens)
print("Total Tokens:", completion.usage.total_tokens)
print("Output:")
print(completion.choices[0].message.content)