from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain


def company_name_generator():
    load_dotenv()

    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    chat_prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful assistant."),
        HumanMessagePromptTemplate.from_template("What is a good name for a company that makes {product}?")
    ])

    chain = LLMChain(llm=chat, prompt=chat_prompt_template)

    print(chain.run("colorful socks"))


if __name__ == "__main__":
    company_name_generator()
