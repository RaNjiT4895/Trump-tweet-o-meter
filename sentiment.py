# sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = "neutral"
    if scores["compound"] >= 0.05:
        sentiment = "positive"
    elif scores["compound"] <= -0.05:
        sentiment = "negative"
    return sentiment, scores
