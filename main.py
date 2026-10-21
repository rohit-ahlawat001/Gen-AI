from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel, Field
from pypdf import PdfReader


PDF_FILE = "LangChain_Beginner_Study_Guide.pdf"
CHUNK_SIZE = 800
NUMBER_OF_CHUNKS = 3


class PDFAnswer(BaseModel):
    """Structured answer returned by the question-answering chain."""

    answer: str = Field(description="Answer based only on the supplied PDF context.")
    found_in_context: bool = Field(
        description="Whether the answer was found in the supplied PDF context."
    )


def read_pdf(file_name):
    # """Read all text from a PDF file."""
    reader = PdfReader(file_name)
    pages = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        pages.append(page_text)

    return "\n".join(pages)


def split_text(text):
    """Split text into chunks without breaking paragraphs when possible."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=200,
    )
    return text_splitter.split_text(text)


load_dotenv()


def create_chatbot():
    """Load the PDF and create the retrieval and answer chain once."""
    pdf_text = read_pdf(PDF_FILE)
    chunks = split_text(pdf_text)

    # Chroma needs an embedding model, not a chat model.
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name="pdf_chunks",
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        temperature=0.3,
        max_output_tokens=300,
    )
    parser = PydanticOutputParser(pydantic_object=PDFAnswer)

    prompt = ChatPromptTemplate.from_template(
        """Answer the question using only the PDF context below.
If the answer is not in the context, set `found_in_context` to false and make
`answer` exactly: I could not find that in the PDF.

{format_instructions}

PDF context:
{context}

Question: {question}
"""
    ).partial(format_instructions=parser.get_format_instructions())

    # The chain formats the prompt, calls Gemini, then converts JSON to PDFAnswer.
    chain = prompt | llm | parser
    return vector_store, chain


def ask_question(question, vector_store, chain):
    """Find relevant PDF content and return one structured answer."""
    relevant_documents = vector_store.similarity_search(question, k=NUMBER_OF_CHUNKS)
    context = "\n\n".join(document.page_content for document in relevant_documents)
    return chain.invoke({"context": context, "question": question})


def run_terminal_chat():
    """Keep a simple terminal version of the chatbot."""
    print("Reading the PDF...")
    vector_store, chain = create_chatbot()
    print("You can now ask questions about the PDF. Type 'exit' to quit.")

    while True:
        question = input("\nAsk a question about the PDF (or type 'exit'): ").strip()

        if question.lower() == "exit":
            print("Goodbye! Have a great day!")
            break

        print("Thinking...")
        response = ask_question(question, vector_store, chain)
        print(f"\nAnswer:\n{response.answer}")


if __name__ == "__main__":
    run_terminal_chat()
