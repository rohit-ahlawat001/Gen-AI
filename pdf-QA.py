import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader


print("📄 Reading PDF...")
reader = PdfReader("JavaScript-Interview-Questions-Answers.pdf")
pdf_content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])


# 2. Define your target question
user_question = input("enter your question") 

# 3. Design the prompt to include BOTH the PDF context and the user's question
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a personal assistant happy to help answer questions based strictly on the provided context."),
    ("user", "Here is the PDF content:\n\n{context}\n\nQuestion: {question}")
])

# 4. Fill the template with the actual PDF data and the question
final_output = prompt_template.format_messages(
    context=pdf_content, 
    question=user_question
)