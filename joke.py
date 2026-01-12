import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": """Please explain the joke: What’s the difference between a poorly dressed man on a unicycle and a well-dressed man on a bicycle? Attire.

""",
        }
    ],
    temperature=1,
    top_p=1,
    model=model
)

print(response.choices[0].message.content)

