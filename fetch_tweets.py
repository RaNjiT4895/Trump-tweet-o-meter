# src/fetch_tweets.py
from sentiment import analyze_sentiment  
from storage import save_tweets
import time
import tweepy
import os
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load environment variables from .env file
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
print("Loaded token:", BEARER_TOKEN)

# Initialize Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def get_trump_tweets(max_results=20):
    query = "Donald Trump -is:retweet lang:en"

    max_results = max(10, min(max_results, 100))  # clamp value between 10 and 100

    response = client.search_recent_tweets(
        query=query,
        tweet_fields=["created_at", "text", "author_id"],
        max_results=max_results
    )

    tweets = response.data if response.data else []
    tweet_list = []
    
    for tweet in tweets:
        sentiment, scores = analyze_sentiment(tweet.text)
        tweet_list.append({
        "text": tweet.text,
        "created_at": tweet.created_at,
        "author_id": tweet.author_id,
        "sentiment": sentiment,
        "scores": scores
        })
    
    time.sleep(60)  # Delay to respect rate limits
    return tweet_list

# For quick testing
if __name__ == "__main__":
    tweets = get_trump_tweets(10)
    save_tweets(tweets)
    print("Saved", len(tweets), "tweets with sentiment.")
