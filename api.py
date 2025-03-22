from fastapi import FastAPI, HTTPException
from utils import extract_news_data, perform_comparative_analysis

app = FastAPI()

@app.post("/get_news_sentiment")
def get_news_sentiment(data: dict):

    # Extract company name from request data
    company = data.get("company")

    # Validate input: Ensure company name is provided
    if not company:
        raise HTTPException(status_code=400, detail="Company name is required")
    
    # Fetch news articles, sentiment scores, and related topics for the company
    news_data, sentiments, topics_list = extract_news_data(company)

    # If no news data is retrieved, return an error response
    if not news_data:
        raise HTTPException(status_code=500, detail="Failed to fetch news articles")
    
    # Perform comparative sentiment analysis on the collected news data
    result = perform_comparative_analysis(news_data, sentiments, topics_list)
    
    # Return the analysis results as JSON response
    return result
