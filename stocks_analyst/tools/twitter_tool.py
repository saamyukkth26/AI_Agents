# import tweepy
# import os

# class TwitterTool:
#     def __init__(self):
#         self.client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'))

#     def search_tweets(self, query, max_results=10):
#         tweets = self.client.search_recent_tweets(query=query, max_results=max_results)
#         return [tweet.text for tweet in tweets.data] if tweets.data else []
