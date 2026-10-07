import os
from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

load_dotenv()

reader = PdfReader("LangChain_Beginner_Study_Guide.pdf")
# docs = loader
text = ""
for page in reader.pages:
    text += page.extract_text()
print(text[:2000])  # Print the first 2000 characters of the extracted text