import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(model="gpt-4o-mini")
response = chat_model.invoke(message)
print(f"\nAI: {response.content}")

