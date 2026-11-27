import os
from dotenv import load_dotenv
from openai import OpenAI

# load the env variables from .env file
load_dotenv()

question = "In one sentence, what is a Docker volume?"
client = OpenAI(
    base_url=os.getenv("LITELLM_URL"),
    api_key=os.environ["DEMO_KEY1"],
)

response = client.chat.completions.create(
    model="chat-default",
    messages=[{"role": "user", "content": question}],
)
print(f"[result] {response.choices[0].message.content}")
print(f"[usage ] tokens:", response.usage.prompt_tokens, "+", response.usage.completion_tokens, "\n")
