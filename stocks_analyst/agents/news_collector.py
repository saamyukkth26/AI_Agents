from crewai import Agent
import google.generativeai as genai
import os
from tools.news_api_tool import NewsApiTool

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini Pro model
llm = genai.GenerativeModel("gemini/gemini-2.0-flash")

news_collector = Agent(
    role='News Collector',
    goal='Gather current stock-related news and tweets.',
    backstory='Expert in financial data collection using search engines and social media.',
    llm=llm
    # tools=[NewsApiTool()]
)
