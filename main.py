from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


PDF_FILE = "LangChain_Beginner_Study_Guide.pdf"
CHUNK_SIZE = 1000
NUMBER_OF_CHUNKS = 3


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

# print("Reading the PDF...")
pdf_text = read_pdf(PDF_FILE)
chunks = split_text(pdf_text)
# print(f"PDF is ready. Created {len(chunks)} chunks.")

# Chroma needs an embedding model, not a chat model.
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
vector_store = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    collection_name="pdf_chunks",
)

llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash", temperature=0.3, max_output_tokens=300)

while True:
    question = input("\nAsk a question about the PDF (or type 'exit'): ").strip()

    if question.lower() == "exit":
        print("Goodbye! Have a great day!")
        break

    # Chroma finds the chunks closest in meaning to the question.
    relevant_documents = vector_store.similarity_search(question, k=NUMBER_OF_CHUNKS)
    context = "\n\n".join(document.page_content for document in relevant_documents)
    prompt = f"""Answer the question using only the PDF context below.
If the answer is not in the context, say: I could not find that in the PDF.

PDF context:
{context}

Question: {question}
"""

    print("Thinking...")
    response = llm.invoke(prompt)
    print(f"\nAnswer:\n{response.content}")
