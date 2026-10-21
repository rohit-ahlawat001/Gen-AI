# Beginner PDF Question & Answer App

Ask questions about `LangChain_Beginner_Study_Guide.pdf`. The program reads the PDF and uses Gemini to answer from its contents.

## What this project does

1. Reads the text from the PDF.
2. Splits long text into smaller chunks.
3. Finds the chunks that best match your question.
4. Sends those chunks and your question to Gemini.
5. Prints Gemini's answer.

## Why this is useful

An AI model cannot reliably use a whole large PDF in every request. Chunks keep the request smaller and help the model focus on the useful part of the document. This is the basic idea behind a PDF chatbot.

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
- `split_text()` breaks that text into chunks of 1,000 characters.
- `get_relevant_text()` picks the three chunks containing the most words from your question.
- `llm.invoke()` sends the selected text and question to Gemini.

## Next improvement

This project uses simple word matching so that the logic is easy to learn. The next step is to replace it with embeddings and a vector database such as Chroma. That will find related ideas even when the question uses different words than the PDF.
