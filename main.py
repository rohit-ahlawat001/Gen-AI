import os
import re

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pypdf import PdfReader


PDF_FILE = "LangChain_Beginner_Study_Guide.pdf"
CHUNK_SIZE = 1000
NUMBER_OF_CHUNKS = 3


def read_pdf(file_name):
    """Read all text from a PDF file."""
    reader = PdfReader(file_name)
    pages = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        pages.append(page_text)

    return "\n".join(pages)


def split_text(text):
    """Split a long PDF into smaller pieces."""
    return [text[start:start + CHUNK_SIZE] for start in range(0, len(text), CHUNK_SIZE)]


def get_relevant_text(chunks, question):
    """Choose chunks that contain the most words from the question."""
    question_words = set(re.findall(r"[a-zA-Z]{3,}", question.lower()))

    ranked_chunks = sorted(
        chunks,
        key=lambda chunk: sum(word in chunk.lower() for word in question_words),
        reverse=True,
    )

    return "\n\n".join(ranked_chunks[:NUMBER_OF_CHUNKS])


def main():
    load_dotenv()

    if not os.getenv("GOOGLE_API_KEY"):
        print("GOOGLE_API_KEY is missing. Add it to your .env file.")
        return

    if not os.path.exists(PDF_FILE):
        print(f"PDF file not found: {PDF_FILE}")
        return

    print("Reading the PDF...")
    pdf_text = read_pdf(PDF_FILE)

    if not pdf_text.strip():
        print("No readable text was found in the PDF.")
        return

    chunks = split_text(pdf_text)
    print(f"PDF is ready. Created {len(chunks)} chunks.")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    while True:
        question = input("\nAsk a question about the PDF (or type 'exit'): ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please type a question.")
            continue

        context = get_relevant_text(chunks, question)
        prompt = f"""Answer the question using only the PDF context below.
If the answer is not in the context, say: I could not find that in the PDF.

PDF context:
{context}

Question: {question}
"""

        print("Thinking...")
        response = llm.invoke(prompt)
        print(f"\nAnswer:\n{response.content}")


if __name__ == "__main__":
    main()
