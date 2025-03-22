import streamlit as st
import requests
from utils import generate_hindi_tts

def fetch_news_sentiment(company):
    api_url = "http://localhost:8000/get_news_sentiment"  # Replace with actual backend API URL
    response = requests.post(api_url, json={"company": company})
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from API")
        return None

def main():
    st.title("News Sentiment Analysis")
    
    company = st.text_input("Enter Company Name:")
    if st.button("Analyze Sentiment"):
        if company:
            result = fetch_news_sentiment(company)
            if result:
                st.subheader("Sentiment Analysis Report")
                st.json(result)  # Display the structured report
                
                summary_text = result["Comparative Analysis"]["Final Sentiment Analysis"]
                audio_file = generate_hindi_tts(summary_text)
                
                with open(audio_file, "rb") as audio:
                    st.audio(audio, format='audio/mp3')
        else:
            st.warning("Please enter a company name")

if __name__ == "__main__":
    main()