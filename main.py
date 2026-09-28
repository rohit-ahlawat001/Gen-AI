import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to a .env file before running the project."
        )

    message = input("Enter a message for the AI: ")
    if not message.strip():
        print("Please enter a message.")
        return

    chat_model = ChatOpenAI(model="gpt-4o-mini")
    response = chat_model.invoke(message)
    print(f"\nAI: {response.content}")


if __name__ == "__main__":
    main()
