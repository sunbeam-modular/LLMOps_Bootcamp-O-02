import os
from dotenv import load_dotenv
from openai import OpenAI

# load the env variables
load_dotenv()

# create the client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

question = "In one sentence, what is a Docker volume?"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": question}],
)

print(response.choices[0].message.content)
print("tokens:", response.usage.prompt_tokens, "+", response.usage.completion_tokens)
