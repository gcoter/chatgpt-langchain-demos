from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)


def call_openai_api_with_langchain():
    load_dotenv()

    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    messages = [
        SystemMessage(content="You are a pirate."),
        HumanMessage(content="Tell the world about the ChatGPT API.")
    ]

    response = chat(messages)

    print(response.content)


if __name__ == "__main__":
    call_openai_api_with_langchain()
