import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')

def ai_writer(chapter_text):
    prompt = f"Rewrite this chapter with a modern, engaging tone:\n\n{chapter_text}"
    response = model.generate_content(prompt)
    return response.text


