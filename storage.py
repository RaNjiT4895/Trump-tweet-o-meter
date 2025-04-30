
# storage.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["trump_tweet_db"]
collection = db["tweets"]

def get_tweets():
    return list(collection.find().sort("created_at", -1))


def save_tweets(tweets):
    if not tweets:
        print("No tweets to save.")
        return

    # Optional: Avoid inserting duplicates by tweet ID or text + created_at
    for tweet in tweets:
        exists = collection.find_one({
            "text": tweet["text"],
            "created_at": tweet["created_at"]
        })
        if not exists:
            collection.insert_one(tweet)
            print("Saved tweet:", tweet["text"][:50])
        else:
            print("Duplicate tweet skipped:", tweet["text"][:50])
