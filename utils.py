import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
import yake
from collections import Counter
from gtts import gTTS
from googletrans import Translator

def extract_news_data(company):
    search_url = f'https://www.google.com/search?q={company}+news&tbm=nws'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        return None, None, None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
    summaries = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    
    news_data = []
    sentiments = []
    topics_list = []
    
    for i in range(min(10, len(articles))):
        title = articles[i].get_text()
        summary = summaries[i].get_text()
        
        # Perform sentiment analysis
        sentiment_score = TextBlob(summary).sentiment.polarity
        sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
        sentiments.append(sentiment)
        
        # Extract topics using YAKE
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(summary)
        topics = [kw[0] for kw in keywords[:3]]  # Top 3 keywords as topics
        topics_list.append(topics)
        
        news_data.append({'Title': title, 'Summary': summary, 'Sentiment': sentiment, 'Topics': ", ".join(topics)})
    
    return news_data, sentiments, topics_list

def generate_hindi_tts(summary_text, filename="sentiment_summary.mp3"):
    # First translate the text from English to Hindi
    translator = Translator()
    try:
        hindi_text = translator.translate(summary_text, src='en', dest='hi').text
    except Exception as e:
        print(f"Translation error: {e}")
        hindi_text = summary_text  # Fallback to original text if translation fails
    
    # Generate TTS with the Hindi text
    tts = gTTS(text=hindi_text, lang="hi")
    tts.save(filename)
    return filename

def perform_comparative_analysis(news_data, sentiments, topics_list):
    sentiment_distribution = Counter(sentiments)
    common_topics = set.intersection(*map(set, topics_list)) if topics_list else set()
    unique_topics = [set(topics) - common_topics for topics in topics_list]
    
    # Get counts for each sentiment type
    positive_count = sentiment_distribution.get("Positive", 0)
    negative_count = sentiment_distribution.get("Negative", 0)
    neutral_count = sentiment_distribution.get("Neutral", 0)
    
    # Create a descriptive sentiment summary
    sentiment_summary = f"Found {positive_count} positive, {negative_count} negative, and {neutral_count} neutral articles."
    
    coverage_differences = []
    for i in range(len(news_data) - 1):
        comparison = f"Article {i+1} discusses {news_data[i]['Topics']}, while Article {i+2} focuses on {news_data[i+1]['Topics']}."
        impact = "This shows how different sources emphasize varying aspects of the company's situation."
        coverage_differences.append({"Comparison": comparison, "Impact": impact})
    
    # Create a list of article details with title, summary, and sentiment
    article_details = []
    for i, article in enumerate(news_data):
        article_details.append({
            "Article": i+1,
            "Title": article['Title'],
            "Summary": article['Summary'],
            "Sentiment": article['Sentiment'],
            "Topics": article['Topics']
        })
    
    comparative_analysis = {
        "Articles": article_details,  # Add individual article details
        "Comparative Analysis": {
            "Comparative Sentiment Score": {
                "Sentiment Distribution": dict(sentiment_distribution),
                "Sentiment Summary": sentiment_summary,
                "Coverage Differences": coverage_differences,
                "Topic Overlap": {
                    "Common Topics": list(common_topics),
                    "Unique Topics": unique_topics
                }
            },
            "Final Sentiment Analysis": f"The latest news coverage on {news_data[0]['Title']} is mostly {max(sentiment_distribution, key=sentiment_distribution.get)}. {sentiment_summary}"
        }
    }
    
    return comparative_analysis

