import os
from dotenv import load_dotenv
from openai import OpenAI
import subprocess
import sys
with open("QuixBugs/python_programs/gcd.py","r",encoding="utf-8") as f:
     code=f.read()
#print(code)
result = subprocess.run(
    [sys.executable, "-m", "pytest", "python_testcases/test_gcd.py"],
    cwd="QuixBugs",
    capture_output=True,
    text=True,
    timeout=10,
)
print(result.returncode)
prompt=f"""下面这个 Python 函数有 bug，测试没有通过。

【代码】
{code}

【测试结果】
{result.stdout}

请修复 bug，只返回修复后的完整代码，不要解释，不要加 ```python 标记。"""
#print(prompt)


load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
client=OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
response = client.chat.completions.create(model="deepseek-flash", messages=[{"role": "user", "content": prompt}])
fixed_code = response.choices[0].message.content
#print(fixed_code)
with open("QuixBugs/python_programs/gcd.py","w",encoding="utf-8") as f:
     f.write(fixed_code)


result2 = subprocess.run(
    [sys.executable, "-m", "pytest", "python_testcases/test_gcd.py"],
    cwd="QuixBugs",
    capture_output=True,
    text=True,
    timeout=10,
)
print(result2.returncode)
print(result2.stdout)