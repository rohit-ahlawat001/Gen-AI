from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel, Field
from pypdf import PdfReader


PDF_FILE = "LangChain_Beginner_Study_Guide.pdf"
CHUNK_SIZE = 1000
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

# The chain formats the prompt, calls Gemini, then converts its JSON to PDFAnswer.
chain = prompt | llm | parser

while True:
    question = input("\n Langchain AI Assisant: ").strip()

    if question.lower() == "exit":
        print("Goodbye! Have a great day!")
        break

    # Chroma finds the chunks closest in meaning to the question.
    relevant_documents = vector_store.similarity_search(question, k=NUMBER_OF_CHUNKS)
    context = "\n\n".join(document.page_content for document in relevant_documents)
    # print("Thinking...")
    response = chain.invoke({"context": context, "question": question})
    print(f"\nAnswer:\n{response.answer}")
