import streamlit as st
import requests

st.title("🏆 Sports News Generator")

# Button to fetch sports news
if st.button("Get Today's Sports News"):
    with st.spinner("Fetching the latest sports news..."):
        response = requests.get("http://127.0.0.1:8000/generate_sports_news")
        
        if response.status_code == 200:
            sports_news = response.json().get("sports_news", "No news available")
            st.write("### 📰 Today's Sports Headlines:")
            st.write(sports_news)
        else:
            st.error("Failed to fetch sports news. Please try again.")
