# src/dashboard.py

import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["trump_tweet_db"]
collection = db["tweets"]

st.set_page_config(page_title="Trump Tweet-O-Meter", layout="wide")
st.title("📊 Trump Tweet-O-Meter")

# Sidebar filter
sentiment_filter = st.sidebar.selectbox("Filter by Sentiment", ["All", "positive", "neutral", "negative"])

# Fetch tweets from MongoDB
def load_tweets():
    if sentiment_filter == "All":
        tweets = list(collection.find().sort("created_at", -1))
    else:
        tweets = list(collection.find({"sentiment": sentiment_filter}).sort("created_at", -1))
    return tweets

tweets = load_tweets()

# Convert to DataFrame for display
df = pd.DataFrame(tweets)
if not df.empty:
    df["created_at"] = pd.to_datetime(df["created_at"])
    df = df[["created_at", "text", "sentiment"]]
    df.columns = ["Timestamp", "Tweet", "Sentiment"]

    st.dataframe(df, use_container_width=True)

    st.bar_chart(df["Sentiment"].value_counts())
else:
    st.warning("No tweets available.")
