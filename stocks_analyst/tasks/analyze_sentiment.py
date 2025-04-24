from crewai import Task
from agents.sentiment_analyzer import sentiment_analyzer

analyze_sentiment_task = Task(
    description='Analyze the sentiment of collected news and tweets.',
    expected_output='List with each source sentiment (positive/negative/neutral).',
    agent=sentiment_analyzer
)
