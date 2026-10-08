import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
client=OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
response = client.chat.completions.create(model="deepseek-flash", messages=[{"role": "user", "content": "你好，用一句话介绍你自己"}])
print(response.choices[0].message.content)
print(api_key)