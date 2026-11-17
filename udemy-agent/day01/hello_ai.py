from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

client = ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        temperature=0.3,
        max_output_tokens=300,
    )

print("=" * 20)
print("My AI Asssistant")