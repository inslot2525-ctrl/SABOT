import google.generativeai as genai

from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(query, context):

    prompt = f"""
You are a senior B2B SaaS sales representative.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find that information in the knowledge base."

Context:

{context}

Question:

{query}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text