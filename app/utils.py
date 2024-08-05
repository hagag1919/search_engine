# utils.py

# utils.py
import re
from flask import Markup

def highlight(text, query):
    highlighted = re.sub(f'({query})', r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return Markup(highlighted)
def format_date(date_str):
    from datetime import datetime
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y')
