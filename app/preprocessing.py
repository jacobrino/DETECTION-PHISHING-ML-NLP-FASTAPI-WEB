# app/preprocessing.py

import re
import html
from bs4 import BeautifulSoup
import nltk

nltk.data.path.clear()
nltk.data.path.append('/var/www/html/INSI/Projet_NLP_Examen/data/ntlk_data')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# URL regex pattern
regex_syntax_url_web = r"(https?://(?:www\.)?\S+|www\.\S+)"
token_url = "urltoken"

import os
import nltk

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # racine Projet_NLP
NLTK_DATA_PATH = os.path.join(BASE_DIR, "data", "ntlk_data")

nltk.data.path.append(NLTK_DATA_PATH)


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def split_camel_case(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text) if isinstance(text, str) else text

def unescape_html(text):
    return html.unescape(text) if isinstance(text, str) else text

def remove_html_tags(text):
    return BeautifulSoup(text, "lxml").get_text() if isinstance(text, str) else text

def reduce_repeated_chars(text):
    return re.sub(r'(.)\1{2,}', r'\1\1', text) if isinstance(text, str) else text

def replace_urls_web(text):
    return re.sub(regex_syntax_url_web, token_url, text) if isinstance(text, str) else text

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text) if isinstance(text, str) else text

def preprocess_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = unescape_html(text)
    text = remove_html_tags(text)
    text = split_camel_case(text)
    text = reduce_repeated_chars(text)
    text = replace_urls_web(text)
    text = remove_punctuation(text)
    text = text.lower()

    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return ' '.join(tokens)

def detect_url(text):
    return 1 if isinstance(text, str) and re.search(regex_syntax_url_web, text) else 0
