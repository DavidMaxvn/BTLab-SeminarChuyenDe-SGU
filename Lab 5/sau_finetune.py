import os
from openai import OpenAI

# Load variables từ .env nếu bạn quản lý key bằng file .env
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
except ImportError:
    pass

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("Thiếu OPENAI_API_KEY. Thiết lập biến môi trường OPENAI_API_KEY trước khi chạy.")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "FUNCTION: {{{def get_square(x: int) -> int:}}}\nCODE:"
        }
    ]
)

print(response.choices[0].message.content)