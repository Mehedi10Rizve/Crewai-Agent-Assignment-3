import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()  # Load environment variables

# Load API key securely
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set up LLM using Gemini 2.0 Flash
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key=GEMINI_API_KEY,
)