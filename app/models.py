from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(50), nullable=True)
    source_name = db.Column(db.String(100))
    author = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(200))
    url_to_image = db.Column(db.String(200), nullable=True)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)

    def __init__(self, source_id, source_name, author, title, description, url, url_to_image, published_at, content):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        
    def __repr__(self):
        return f'<NewsArticle {self.title}>'