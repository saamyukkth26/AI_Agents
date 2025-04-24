from crewai import Crew
from tasks.collect_news import collect_news_task
from tasks.analyze_sentiment import analyze_sentiment_task
from tasks.generate_advice import generate_advice_task
from agents.news_collector import news_collector
from agents.sentiment_analyzer import sentiment_analyzer
from agents.financial_strategist import financial_strategist

crew = Crew(
    agents=[news_collector, sentiment_analyzer, financial_strategist],
    tasks=[collect_news_task, analyze_sentiment_task, generate_advice_task],
    verbose=True
)

result = crew.kickoff()
print(result)
