import requests
from app.models import NewsArticle, db
from config import Config
from datetime import datetime

def fetch_news(source_id,):
    url = f"{Config.NEWS_API_BASE_URL}/{source_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        for article in articles:
            news_article = NewsArticle(
                source_id=article['source'].get('id'),
                source_name=article['source']['name'],
                author=article.get('author'),
                title=article['title'],
                description=article.get('description'),
                url=article['url'],
                url_to_image=article.get('urlToImage'),
                published_at=datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                content=article.get('content')
            )
            db.session.add(news_article)
        db.session.commit()
    else:
        print(f"Failed to fetch news: {response.status_code}")
        
def fetch_all_news():
    for source_id in Config.NEWS_SOURCES:
        fetch_news(source_id)       