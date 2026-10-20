# 🔎 Tool-Using Research Agent

An AI-powered research assistant built with Python and the Groq API. It searches the web, fetches relevant webpage content, generates research answers with source citations, and checks claims against available evidence.

## 🚀 Features

- 🔍 Web search using DuckDuckGo (`ddgs`)
- 🤖 LLM-powered research using the Groq API
- 🧭 Agent decision loop to select the next action
- 🌐 Fetches relevant webpage content
- 🔗 Generates answers with source citations
- ✅ Verifies answer claims against collected evidence
- 🔢 Validates citation numbers against available sources
- 🔁 Limits agent actions using a maximum step budget
- 🧹 Handles duplicate search results
- 🔐 Loads API credentials from environment variables

## 🛠️ Tech Stack

- Python
- Groq API
- DuckDuckGo Search (`ddgs`)
- Requests
- `python-dotenv`

## ⚙️ How It Works

1. The user enters a research question.
2. The agent selects an action, such as searching the web, fetching a webpage, or finishing the research.
3. Search results are collected and relevant webpages are fetched.
4. The language model generates an answer using the collected research.
5. The answer includes source citations and a source list.
6. A claim-verification step compares answer claims against available evidence.
7. Citation numbers are checked against the collected sources.

The agent operates within a maximum step budget to limit the number of actions per research task.

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/nagadevibarthala-source/tool-using-research-agent.git
cd tool-using-research-agent
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install python-dotenv ddgs groq requests
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key. Never commit your real API key to GitHub.

### 5. Run the agent

```bash
python main.py
```

Enter a research question when prompted.

## 🧪 Example Research Questions

- What is Agentic AI and how is it used in automation?
- How can AI agents automate recruitment for companies?
- What are the benefits and risks of AI-powered automation?

The agent's results depend on the search results, webpage content, and language model output.

## 🔐 Security and Limitations

- Keep the `.env` file and API key private.
- Ensure `.env` is excluded through `.gitignore`.
- Verify important information against the original sources.
- Claim verification depends on the quality and completeness of the fetched evidence; a supported claim is not a guarantee of truth.
- Search results and webpages may be incomplete, unavailable, or outdated.
- The agent uses a finite action budget and may finish before gathering every relevant source.

## 🎯 Project Goal

This project demonstrates how an AI agent can use external search and webpage-fetching tools with a large language model to research questions, generate cited answers, and check claims against collected evidence.

## 👩‍💻 Author

Built as a hands-on Python and Agentic AI learning project.
