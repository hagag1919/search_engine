import os

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NEWS_API_BASE_URL = 'https://saurav.tech/NewsAPI/everything'
    NEWS_SOURCES = ['cnn', 'bbc-news', 'fox-news', 'google-news']