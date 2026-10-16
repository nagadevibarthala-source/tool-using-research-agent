# 🔎 Tool-Using Research Agent

An AI-powered research assistant that searches the web, summarizes relevant information using a Large Language Model (LLM), and provides source links to help users explore answers.

## 🚀 Features

- 🔍 Web search using DuckDuckGo
- 🤖 AI-generated research summaries using the Groq API
- 🔗 Source URLs for further reading
- 🧹 Removes duplicate and incomplete search results
- 🐍 Built with Python

## 🛠️ Tech Stack

- Python
- Groq API
- DuckDuckGo Search (`ddgs`)
- `python-dotenv`

## ⚙️ How It Works

1. The user enters a research question.
2. The agent searches the web for relevant information.
3. Search results are passed to the language model.
4. The model generates a summary based on the available results.
5. The response includes source links for further reading.

## 📦 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/nagadevibarthala-source/tool-using-research-agent.git
   ```

2. Open the project folder:

   ```bash
   cd tool-using-research-agent
   ```

3. Create and activate a virtual environment on Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install the required packages:

   ```bash
   pip install python-dotenv ddgs groq
   ```

5. Create a `.env` file in the project root and add your own Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Never upload your real API key to GitHub.

6. Run the application:

   ```bash
   python main.py
   ```

7. Enter a research question when prompted.

## 🔐 Security

API keys and environment files should remain private. The `.env` file is excluded through `.gitignore`.

## 🎯 Project Goal

This project demonstrates how an AI application can use an external search tool and an LLM together to answer research questions with source links.

## 👩‍💻 Author

Built as a hands-on Python and Agentic AI learning project.