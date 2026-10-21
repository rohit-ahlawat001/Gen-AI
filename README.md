# Beginner PDF Question & Answer App

Ask questions about `LangChain_Beginner_Study_Guide.pdf`. The program reads the PDF and uses Gemini to answer from its contents.

## What this project does

1. Reads the text from the PDF.
2. Splits long text into smaller chunks.
3. Creates embeddings and stores the chunks in Chroma vector database.
4. Finds the chunks closest in meaning to your question.
5. Sends those chunks and your question to Gemini.
6. Prints Gemini's answer.

## Why this is useful

An AI model cannot reliably use a whole large PDF in every request. Chunks keep the request smaller and help the model focus on the useful part of the document. Chroma uses embeddings to find similar meaning, so a question does not need to use the exact same words as the PDF.

## Setup

### 1. Install Python

Install Python 3.12 or 3.13 and select **Add Python to PATH** during installation. Close and reopen PowerShell, then check:

```powershell
python --version
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If the existing `.venv` gives an error, delete that `.venv` folder first and run these commands again.

### 3. Install the packages

```powershell
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a file called `.env` in this folder and add:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

Never upload `.env` to GitHub.

### 5. Run the project

```powershell
python main.py
```

Ask a question, for example:

```text
What is LangChain?
```

Type `exit` when you are finished.

## How the code works

- `read_pdf()` gets text from every page of the PDF.
- `RecursiveCharacterTextSplitter` breaks text into chunks of 1,000 characters while trying to keep paragraphs together. Each chunk overlaps by 100 characters, so important text at a chunk boundary is not lost.
- `GoogleGenerativeAIEmbeddings` converts each chunk into numbers that represent its meaning.
- `Chroma` stores those embeddings in a vector database.
- `similarity_search()` gets the three chunks most related to your question.
- `llm.invoke()` sends the selected text and question to Gemini.

## Important

The vector database is in memory. It is built each time you start the program, so the code stays simple and the PDF can be changed without managing old data.
