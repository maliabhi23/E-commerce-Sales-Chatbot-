import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Now access the key securely
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(message):
    try:
        response = model.generate_content(message)
        return response.text.strip()
    except Exception as e:
        return f"Error from Gemini: {str(e)}"
