from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

USER_PROMPT = """
def print_fibonacci_sequence(n: int) -> None:
"""

SYSTEM_PROMPT = (
    "You will be provided with a Python function signature. "
    "Your task is to implement the function. Return code only."
)

def get_code_with_instructions(code: str) -> str:
    return code + "\n# Complete this code"

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model=model,
    temperature=1,
    n=2,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": get_code_with_instructions(USER_PROMPT)}
    ],
)

print("=== LAB 2.3 ===")
for i, choice in enumerate(completion.choices, start=1):
    output = choice.message.content
    print(f"\n--- Output {i} ---")
    print(output)