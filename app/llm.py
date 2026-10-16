from google import genai
from app.config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_reply(history):
    """Send our manually managed conversation history to Gemini."""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=history,
    )
    if not response.text:
        raise RuntimeError("The model returned an empty response.")
    return response.text
