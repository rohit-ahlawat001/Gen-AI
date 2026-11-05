from pathlib import Path
from unittest import loader
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "LangChain_Beginner_Study_Guide.pdf"

loader = PyPDFLoader(file_path = pdf_path)

docs = loader.load()

print(docs)