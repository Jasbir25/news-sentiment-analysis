import os
import subprocess
import streamlit as st
import requests
from utils import generate_hindi_tts

# Start FastAPI backend as a subprocess
if 'backend' not in st.session_state:
    st.session_state.backend = subprocess.Popen(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])

# Function to fetch sentiment analysis results
def fetch_news_sentiment(company):
    api_url = "http://localhost:8000/get_news_sentiment"
    response = requests.post(api_url, json={"company": company})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from API")
        return None

# Streamlit UI
st.title("News Sentiment Analysis")
company = st.text_input("Enter Company Name:")
if st.button("Analyze Sentiment"):
    if company:
        result = fetch_news_sentiment(company)
        if result:
            st.subheader("Sentiment Analysis Report")
            st.json(result)
            summary_text = result["Comparative Analysis"]["Final Sentiment Analysis"]
            audio_file = generate_hindi_tts(summary_text)
            with open(audio_file, "rb") as audio:
                st.audio(audio, format='audio/mp3')
    else:
        st.warning("Please enter a company name")
