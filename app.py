import streamlit as st
from storage import get_tweets

st.title("Trump Tweet-O-Meter")

tweets = get_tweets()
if tweets:
    for tweet in tweets:
        st.write(f"🕒 {tweet['created_at']}")
        st.write(f"🗣️ {tweet['text']}")
        st.markdown("---")
else:
    st.write("No tweets found.")
