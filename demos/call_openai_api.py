import os
import openai
from dotenv import load_dotenv


def call_openai_api():
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    messages = [
        {"role": "system", "content": "You are a pirate."},
        {"role": "user", "content": "Tell the world about the ChatGPT API."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    call_openai_api()
