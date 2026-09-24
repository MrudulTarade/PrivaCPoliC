import os
from openai import OpenAI


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def create_answer(context, question):

    prompt = f"""
You are a privacy policy assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer cannot be found in the context, say:
"I could not find this information in the privacy policy."

Do not make up information.
Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:groq",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content