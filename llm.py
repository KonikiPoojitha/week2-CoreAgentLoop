


import os
from dotenv import load_dotenv

load_dotenv()


def ask_llm(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "GROQ_API_KEY is not configured."

    try:
        from groq import Groq
    except ImportError:
        return "Groq package is not installed."

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
