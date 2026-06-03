import google.generativeai as genai

from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def classify_intent(query: str) -> str:

    prompt = f"""
You are an intent classifier.

Possible intents:

pricing
objection
competitor
feature
closing

Examples:

Question: What are your pricing plans?
Intent: pricing

Question: Your competitor is cheaper.
Intent: competitor

Question: I am not sure your solution is reliable.
Intent: objection

Question: Does your platform support API integration?
Intent: feature

Question: I want to schedule a demo.
Intent: closing

Question:
{query}

Return ONLY the intent label.
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()