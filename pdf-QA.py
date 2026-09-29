import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader


print("📄 Reading PDF...")
reader = PdfReader("JavaScript-Interview-Questions-Answers.pdf")
pdf_content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
