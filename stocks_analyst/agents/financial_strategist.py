from crewai import Agent
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini Pro model
llm = genai.GenerativeModel("gemini/gemini-2.0-flash")

financial_strategist = Agent(
    role='Financial Strategist',
    goal='Give stock advice based on news and sentiment analysis.',
    backstory='A hedge fund analyst known for accurate data-backed predictions.',
    llm=llm
)
