import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

load_dotenv()

loader = PdfReader("LangChain_Beginner_Study_Guide.pdf")
