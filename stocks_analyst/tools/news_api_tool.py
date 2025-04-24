import requests
import os

class NewsApiTool:
    def __init__(self):
        self.api_key = os.getenv("NEWSAPI_KEY")

    def get_news(self, query, language="en"):
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "language": language,
            "sortBy": "publishedAt",
            "apiKey": self.api_key
        }
        response = requests.get(url, params=params)
        articles = response.json().get("articles", [])
        return [{"title": a["title"], "url": a["url"], "description": a["description"]} for a in articles]
