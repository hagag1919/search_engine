from flask import render_template, request
from app import app
from app.data_fetcher import fetch_all_news
from app.models import NewsArticle
from app.search_engine import SearchEngine

# Initialize and build the search engine index
search_engine = SearchEngine()
# Fetch news articles and build the search index
fetch_all_news()
# Build the search index
search_engine.build_index()

@app.route('/')
def index():
    articles = NewsArticle.query.all()
    return render_template('index.html', articles=articles)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        articles = search_engine.search(query)
    else:
        articles = []
    return render_template('search_results.html', articles=articles, query=query)
