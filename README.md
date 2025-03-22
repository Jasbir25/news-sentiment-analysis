# News Sentiment Analysis

This project analyzes the sentiment of news articles related to a given company. It extracts news data, performs sentiment analysis, and provides insights into sentiment distribution and topic overlap. Additionally, it generates a Hindi text-to-speech (TTS) summary of the sentiment analysis.

## Project Overview
This application is designed to run seamlessly on **Hugging Face Spaces**, where both the FastAPI backend and Streamlit frontend are executed within the same script. It:
- Fetches the latest news articles for a given company.
- Performs sentiment analysis using TextBlob.
- Extracts keywords using YAKE.
- Provides a comparative sentiment analysis report.
- Generates a Hindi TTS summary using gTTS.

## How It Works
1. The FastAPI backend handles requests for sentiment analysis.
2. The Streamlit frontend provides an interactive UI for user input.
3. Both processes run in the same script within Hugging Face Spaces.

## Setup Instructions
Hugging Face Spaces automatically installs dependencies from `requirements.txt`. If running locally, install dependencies with:
```sh
pip install -r requirements.txt
```

To start the application locally, run:
```sh
python app.py
```

## Running on Hugging Face Spaces
- The script initializes the FastAPI backend.
- Streamlit serves as the main entry point while communicating with FastAPI in the background.
- The app runs as a single process, making it suitable for Hugging Face Spaces.

## Technologies Used
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **BeautifulSoup** (Web Scraping)
- **TextBlob** (Sentiment Analysis)
- **YAKE** (Keyword Extraction)
- **Google Translate API** (Translation)
- **gTTS** (Text-to-Speech)

## Notes
- The news extraction relies on Google search results, which may have access restrictions.
- Ensure your network allows requests to Google search for proper functionality.
- The Hindi TTS output may not be perfect due to translation limitations.

---
### Author: Jasbir Singh
