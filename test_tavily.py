import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

print("Testing Tavily...")

response = client.search(
    query="Latest developments in artificial intelligence",
    max_results=3
)

print(response)
print("Tavily working!")