
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0,
    google_api_key=api_key,
    max_retries=0,
    timeout=20
)

print("Testing Gemini...", flush=True)

try:
    response = llm.invoke("Say hello in one sentence.")
    print("SUCCESS:", response.content)

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))
