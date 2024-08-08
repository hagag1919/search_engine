
# Learn Search Engine Concepts

This repository provides a simple implementation of a search engine using Flask and SQLAlchemy. It demonstrates the basic concepts of indexing, searching, and highlighting matched text in search results.

# Search Terminology

## Index
An index is a data structure that improves the speed of data retrieval operations on a database table. In the context of search engines, an index is created to allow quick lookup of documents that contain specific words or phrases. It maps terms to the documents in which they appear.

## Documents
Documents are the basic units of information that are indexed and searched. In a search engine, a document can be any piece of text, such as a web page, a PDF file, or a database record. Each document is assigned a unique identifier and is processed to extract searchable content.

## Tokenization
Tokenization is the process of breaking down text into smaller units called tokens, typically words or phrases. This is a crucial step in text processing for search engines, as it allows the system to analyze and index the content effectively. For example, the sentence "The quick brown fox" would be tokenized into ["The", "quick", "brown", "fox"].

## Edge N-Grams
Edge n-grams are a type of n-gram that captures the beginning part of a word. They are used to improve search performance by allowing partial matches. For example, the word "search" can be broken down into edge n-grams like ["s", "se", "sea", "sear", "searc", "search"]. This helps in matching queries like "sea" or "sear" to the word "search".

## Segments
Segments refer to the individual parts of an index. In large-scale search engines, the index is often divided into multiple segments to manage and update the data more efficiently. Each segment is a self-contained index that can be searched independently. When a search query is executed, the results from all segments are combined to produce the final output.

## Query Parser
A query parser is a component of a search engine that interprets and processes user queries. It translates the user's search input into a format that the search engine can understand and execute. The query parser handles various aspects such as parsing keywords, handling operators (AND, OR, NOT), and managing special characters or syntax.


# News Search Engine

This repository contains a simple news search engine built with Flask and SQLAlchemy. The search engine allows users to search for news articles and highlights the matched text in the search results.

## Features

- Fetches news articles from a specified source (e.g., CNN).
- Indexes articles for fast search.
- Highlights matched text in search results.

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- SQLAlchemy

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/hagag1919/search_engine.git
    cd news-search-engine
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

Ensure you have a configuration file (e.g., `config.py`) with the necessary settings for your Flask application and database.

### Running the Application

1. **Set the Flask app environment variable**:

    ```sh
    set FLASK_APP=app
    ```

2. **Run the Flask application**:

    ```sh
    flask run
    ```

3. **Access the application**:

    Open your web browser and navigate to `http://127.0.0.1:5000/`.
    '''

### You can use this app in any type of data

**By replacing the data fetching and indexing logic**: 

1. **Update the Data Fetcher**: Modify the `data_fetcher.py` to fetch data from your desired source. Ensure the data is stored in the `NewsArticle` model or a similar model that fits your data structure.

    ```python
    # data_fetcher.py
    def fetch_data(source):
        # Implement logic to fetch data from the new source
        pass
    ```

2. **Update the Models**: Ensure your data model in `models.py` matches the structure of the new data source.

    ```python
    # models.py
    from app import db

    class YourDataModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        description = db.Column(db.String, nullable=False)
        content = db.Column(db.Text, nullable=False)
        url = db.Column(db.String, nullable=False)
    ```

3. **Update the Search Engine**: Modify the `search_engine.py` to index and search the new data model.

    ```python
    # search_engine.py
    from app.models import YourDataModel

    def search_data(query):
        if not query:
            return []

        data = YourDataModel.query.filter(
            YourDataModel.title.ilike(f'%{query}%') |
            YourDataModel.description.ilike(f'%{query}%') |
            YourDataModel.content.ilike(f'%{query}%')
        ).all()

        for item in data:
            item.title = highlight_text(item.title, query)
            item.description = highlight_text(item.description, query)
            item.content = highlight_text(item.content, query)

        return data
    ```

4. **Update the Routes**: Ensure your Flask routes use the updated search function and data model.

    ```python
    # routes.py
    from flask import render_template, request
    from app import app
    from app.data_fetcher import fetch_data
    from app.models import YourDataModel
    from app.search_engine import search_data

    @app.route('/')
    def index():
        fetch_data('your_source')
        data = YourDataModel.query.all()
        return render_template('index.html', data=data)

    @app.route('/search', methods=['GET'])
    def search():
        query = request.args.get('q')
        data = search_data(query)
        return render_template('search_results.html', data=data, query=query)
    ```

5. **Update the Templates**: Ensure your templates can display the new data structure.

    - `index.html`

        ```html
        !DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Search Engine</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
        </head>
        <body>
            <div class="search-container">
                <input type="text" id="search-bar" placeholder="Search">
                <button id="search-btn">Search</button>
            </div>
            <ul id="results-list"></ul>
            <script src="{{ url_for('static', filename='js/script.js') }}"></script>
        </body>
        </html>
        ```

   

By following these steps, you can adapt this search engine to work with any type of data.
