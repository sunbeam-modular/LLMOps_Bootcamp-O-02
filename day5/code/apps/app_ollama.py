import os
import ollama
from dotenv import load_dotenv

# load the env variables
load_dotenv()

# create the client
client = ollama.Client(host=os.getenv("OLLAMA_URL"))

question = "In one sentence, what is a Docker volume?"
response = client.chat(
    model="llama3.2:1b",
    messages=[{"role": "user", "content": question}],
)
print(response.message.content)
print("tokens:", response.prompt_eval_count, "+", response.eval_count)
