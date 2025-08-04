import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')

def ai_reviewer(text):
    prompt = f"Review the following chapter and improve clarity, grammar, and tone:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text


