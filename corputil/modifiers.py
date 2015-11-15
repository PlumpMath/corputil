import re
import nltk

from .utils import get_stopwords


tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
stopwords = get_stopwords('german')


def to_words(doc):
    for sentence in to_sentences(doc):
        letters_only = re.sub(r'[^a-zäöüA-ZÖÄÜß]', ' ', sentence)
        words = letters_only.lower().split()
        words = [word for word in words if word not in stopwords]
        yield words


def to_sentences(doc):
    raw_sentences = tokenizer.tokenize(doc.strip())
    for sentence in raw_sentences:
        yield sentence
