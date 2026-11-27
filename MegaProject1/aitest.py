from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

groqApiKey = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=groqApiKey,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    max_tokens=150,  # Hard limit on output tokens
    messages=[
        {"role": "system", "content": "Reply in 1 or 2 short sentences only."},
        {"role": "user", "content": "Who is Muhammad Ali Jinnah"}
    ]
    )
print(response.choices[0].message.content)