
import os
from dotenv import load_dotenv
from groq import Groq
from search_tool import search_web

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Groq API key missing. Check your .env file.")
    raise SystemExit

client = Groq(api_key=api_key)

question = input("What do you want to research? ")

print("\nSearching the web...\n")

results = search_web(question, max_results=5)
print("WEB SEARCH RESULTS\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. {result['title']}")
    print(f"   URL: {result['url']}")
    print(f"   Summary: {result['snippet'][:200]}")
    print()
if not results:
    print("No search results found. Try another question.")
    raise SystemExit

context = ""

for i, result in enumerate(results, start=1):
    context += (
        f"\nSource {i}: {result['title']}\n"
        f"URL: {result['url']}\n"
        f"Information: {result['snippet']}\n"
    )


prompt = f"""
You are a careful research assistant.

Answer the user's question using ONLY the supplied search results.

Rules:
1. Attach source citations like [1] or [2] to factual claims.
2. Use only source numbers that appear in the supplied results.
3. Do not invent facts, statistics, quotations, or source details.
4. If the sources do not support a claim, say that the information could not be verified.
5. End with a Sources section listing the source number, title, and URL.

User question:
{question}

Search results:
{context}
"""

print("Generating answer...\n")

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    print("RESEARCH ANSWER\n")
    print(response.choices[0].message.content)

except Exception as error:
    print("AI request failed.")
    print("Error type:", type(error).__name__)
    print("Please check the model and API limits.")
