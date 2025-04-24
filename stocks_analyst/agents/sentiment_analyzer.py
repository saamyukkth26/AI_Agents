from crewai import Agent
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini Pro model
llm = genai.GenerativeModel("gemini/gemini-2.0-flash")

sentiment_analyzer = Agent(
    role='Sentiment Analyzer',
    goal='Analyze tone of collected data and determine public sentiment.',
    backstory='A sentiment analyst using NLP to gauge market trends from public opinion.',
    llm=llm
    # tools=[SentimentModel()]
)
