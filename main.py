import os
from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

reader = PdfReader("LangChain_Beginner_Study_Guide.pdf")
# docs = loader
text = ""
for page in reader.pages:
    text += page.extract_text()
# print(text[:200])  # Print the first 2000 characters of the extracted text

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    # length_function=len
)

chunks = text_splitter.split_text(text)
print("Total chunks:", len(chunks))
print(chunks[0])
