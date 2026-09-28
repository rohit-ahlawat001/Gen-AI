import os
from dotenv import load_dotenv
from langchain_openAI import ChatOpenAI

message = input("Enter a message for the Search: ")
if not message.strip():
 print("Please enter a message.")
#  return
chat_model = ChatOpenAI(model="gpt-4o-mini")
response = chat_model.invoke(message)
print(f"\nAI: {response.content}")

