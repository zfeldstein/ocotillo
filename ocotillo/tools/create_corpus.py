import spacy
from web.html_to_text import html_to_text
from spacy.matcher import Matcher, PhraseMatcher

nlp = spacy.load('en_core_web_sm')

def create_text_file(url=None):
    url = 'https://www.space.com/16907-what-is-the-temperature-of-mars.html'
    text_data = html_to_text(url)

