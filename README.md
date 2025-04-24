# AI_Agents
Developing AI agents, crew agents (multi agents)...


# 📈 Real-Time Stock Market Analyst (CrewAI + Gemini 2.0)
 
A multi-agent AI system built using **CrewAI** and **Gemini 2.0 Flash** that provides real-time news collection, sentiment analysis, and financial strategy generation based on stock market events.
 
---
 
## 🚀 Project Overview
 
This project simulates a real-world AI analyst team that:
- Collects the latest financial news and tweets related to tech stocks.
- Analyzes sentiment from the gathered content.
- Generates strategic investment advice based on market sentiment.
 
It uses the **CrewAI** framework to coordinate tasks between multiple LLM-powered agents.
 
---
 
## 🧠 Workflow & Architecture
 
### 👥 Agents
1. **News Collector**
   - Role: Gathers current tech stock-related news and tweets.
   - Powered by: Gemini 2.0 Flash + News API
 
2. **Sentiment Analyzer**
   - Role: Analyzes the tone of collected news articles and tweets.
 
3. **Financial Strategist**
   - Role: Generates actionable investment advice based on sentiment.
 
### 🛠 Tasks
- `collect_news_task`: Instructs News Collector to fetch the latest stock news.
- `analyze_sentiment_task`: Instructs Sentiment Analyzer to evaluate market tone.
- `generate_advice_task`: Instructs Financial Strategist to provide trading insights.
 
### 🔧 Tools
- `NewsApiTool`: Integrates with the [NewsAPI](https://newsapi.org/) to fetch real-time news data via HTTP requests.
 
### 🧬 Execution Flow
1. The Crew starts when `crew.kickoff()` is called.
2. `News Collector` agent fetches news using `NewsApiTool`.
3. `Sentiment Analyzer` analyzes the collected headlines and summaries.
4. `Financial Strategist` interprets the sentiment and generates strategy/advice.
5. Final result is printed to the console.
 
---

