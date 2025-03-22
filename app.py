import streamlit as st
import requests
from utils import generate_hindi_tts

# Function to fetch sentiment analysis results from FastAPI backend
def fetch_news_sentiment(company):
    api_url = "http://localhost:8000/get_news_sentiment"  # API endpoint for fetching news sentiment
    response = requests.post(api_url, json={"company": company})
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        st.error("Failed to fetch data from API")   # Show error message if API request fails
        return None

# Streamlit UI main function
def main():
    st.title("News Sentiment Analysis") # Application title
    
    # User input for company name
    company = st.text_input("Enter Company Name:")

    # Trigger analysis when the button is clicked
    if st.button("Analyze Sentiment"):
        if company:
            result = fetch_news_sentiment(company)  # Call API to fetch sentiment report
            if result:
                st.subheader("Sentiment Analysis Report")
                st.json(result)  # Display the structured report

                # Extract final sentiment summary for text-to-speech conversion
                summary_text = result["Comparative Analysis"]["Final Sentiment Analysis"]
                audio_file = generate_hindi_tts(summary_text)
                
                # Dsiplay Hindi TTS output
                with open(audio_file, "rb") as audio:
                    st.audio(audio, format='audio/mp3')
        else:
            st.warning("Please enter a company name")   # Prompt user if no input is provided

if __name__ == "__main__":
    main()
