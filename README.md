# News Sentiment Analysis

This project analyzes the sentiment of news articles related to a given company. It extracts news data, performs sentiment analysis, and provides insights into sentiment distribution and topic overlap. Additionally, it generates a Hindi text-to-speech (TTS) summary of the sentiment analysis.

## Project Structure

### 1. `api.py` (FastAPI Backend)
This file implements a FastAPI backend that processes company-related news articles and performs sentiment analysis.

- **Endpoint:** `POST /get_news_sentiment`
- **Functionality:**
  - Accepts a company name as input.
  - Fetches relevant news articles.
  - Performs sentiment analysis and topic extraction.
  - Returns a structured sentiment analysis report.

### 2. `utils.py` (Utility Functions)
This file contains helper functions for extracting news, performing sentiment analysis, and generating a Hindi TTS summary.

- **`extract_news_data(company)`**
  - Fetches Google News articles related to the company.
  - Extracts titles, summaries, sentiment scores, and keywords.
  
- **`perform_comparative_analysis(news_data, sentiments, topics_list)`**
  - Analyzes sentiment distribution.
  - Identifies common and unique topics across articles.
  - Generates a comparative sentiment report.
  
- **`generate_hindi_tts(summary_text, filename="sentiment_summary.mp3")`**
  - Translates English sentiment summary to Hindi.
  - Converts the Hindi text into speech and saves it as an MP3 file.

### 3. `app.py` (Streamlit Frontend)
This file provides a simple Streamlit-based user interface for interacting with the backend.

- **User Workflow:**
  - Enter the company name in a text input field.
  - Click the "Analyze Sentiment" button.
  - The app fetches sentiment analysis results from the FastAPI backend.
  - Displays the structured sentiment report in JSON format.
  - Generates and plays a Hindi TTS summary of the sentiment analysis.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
```

### 2. Run the FastAPI Backend
```sh
uvicorn api:app --reload
```

### 3. Run the Streamlit App
```sh
streamlit run app.py
```

## Usage
1. Start the FastAPI server.
2. Open the Streamlit app in the browser.
3. Enter a company name and click "Analyze Sentiment".
4. View the analysis results and listen to the Hindi TTS summary.

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
- Ensure that your network allows requests to Google search for proper functionality.
- The Hindi TTS output may not be perfect due to translation limitations.

---
### Author: Jasbir Singh
