from app.models import NewsArticle
from app.utils import highlight
from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import re

class SearchEngine:
    def __init__(self):
        self.index = defaultdict(list)
        self.stemmer = PorterStemmer()

    def build_index(self):
        """Index all articles for fast search."""
        articles = NewsArticle.query.all()
        for article in articles:
            words = self.tokenize(article.title) + \
                    self.tokenize(article.description) + \
                    self.tokenize(article.content)
            for word in words:
                self.index[word.lower()].append(article.id)
        print(f"Indexed {len(articles)} articles.")

    def tokenize(self, text):
        """Tokenize text into words, handling basic stemming and synonyms."""
        # Basic tokenization and lowercasing
        words = re.findall(r'\w+', text.lower())
        
        # Apply stemming
        stemmed_words = [self.stemmer.stem(word) for word in words]
        
        # Expand with synonyms
        expanded_words = set(stemmed_words)  # Use a set to avoid duplicates
        for word in stemmed_words:
            synonyms = self.get_synonyms(word)
            expanded_words.update(synonyms)
        
        return list(expanded_words)

    def get_synonyms(self, word):
        """Get a list of synonyms for a given word using WordNet."""
        synonyms = set()
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonym = lemma.name().replace('_', ' ')
                stemmed_synonym = self.stemmer.stem(synonym)
                synonyms.add(stemmed_synonym)
        return synonyms

    def search(self, query):
        """Search for articles matching the query."""
        query_words = self.tokenize(query)
        article_scores = defaultdict(int)

        for word in query_words:
            for article_id in self.index.get(word, []):
                article_scores[article_id] += 1

        # Sort articles by score (higher is better)
        sorted_articles = sorted(article_scores.items(), key=lambda x: x[1], reverse=True)
        article_ids = [article_id for article_id, score in sorted_articles]
        articles = NewsArticle.query.filter(NewsArticle.id.in_(article_ids)).all()

        # Highlight the query in the articles
        highlighted_articles = self.highlight_matches(articles, query_words)
        return highlighted_articles

    def highlight_matches(self, articles, query_words):
        """Highlight the matches in the articles."""
        for article in articles:
            article.title = highlight(article.title, query_words)
            article.description = highlight(article.description, query_words)
            article.content = highlight(article.content, query_words)
        return articles


