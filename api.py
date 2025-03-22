from fastapi import FastAPI, HTTPException
from utils import extract_news_data, perform_comparative_analysis

app = FastAPI()

@app.post("/get_news_sentiment")
def get_news_sentiment(data: dict):
    company = data.get("company")
    if not company:
        raise HTTPException(status_code=400, detail="Company name is required")
    
    news_data, sentiments, topics_list = extract_news_data(company)
    if not news_data:
        raise HTTPException(status_code=500, detail="Failed to fetch news articles")
    
    result = perform_comparative_analysis(news_data, sentiments, topics_list)
    return result
