from textblob import TextBlob

class SentimentModel:
    def analyze(self, text_list):
        results = []
        for text in text_list:
            polarity = TextBlob(text).sentiment.polarity
            sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
            results.append({"text": text, "sentiment": sentiment, "score": polarity})
        return results
