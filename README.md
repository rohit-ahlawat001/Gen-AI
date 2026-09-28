# Beginner LangChain Message Project

A small Python command-line program that sends one message to an OpenAI chat model through LangChain and prints the reply.

## 1. Create and activate a virtual environment

In PowerShell, open this project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2. Install the packages

```powershell
pip install -r requirements.txt
```

## 3. Add your OpenAI API key

Copy the example environment file and edit the copy:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the example value with your OpenAI API key. Keep `.env` private; it is excluded from Git.

## 4. Run the project

```powershell
python main.py
```

Type a message when prompted. The program sends it to the `gpt-4o-mini` model and prints the response.
