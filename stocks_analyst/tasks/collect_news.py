from crewai import Task
from agents.news_collector import news_collector

collect_news_task = Task(
    description='Collect latest news and tweets about tech stocks.',
    expected_output='Bullet points with links and text summaries.',
    agent=news_collector
)
