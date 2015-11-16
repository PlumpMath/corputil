import re
import nltk
from textblob_de import TextBlobDE as TextBlob

from .utils import get_stopwords


tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
stopwords = get_stopwords('german')
pattern = re.compile(r'\W')
wanted_tags = {'NN', 'NE', 'NNS', 'NNP'}


def to_words(doc):
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words]
    yield words


def to_words_sl(doc):
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words if word not in stopwords]
    yield words


def to_keywords(doc):
    letters_only = pattern.sub(' ', doc)
    blob = TextBlob(letters_only)
    keywords = [word.lower() for word, tag in blob.tags
                if word.lower() not in stopwords and tag in wanted_tags]
    yield keywords


def to_sentences(doc):
    raw_sentences = tokenizer.tokenize(doc.strip())
    for sentence in raw_sentences:
        yield sentence


def sentence_to_words(doc):
    for sentence in to_sentences(doc):
        letters_only = pattern.sub(' ', sentence)
        words = letters_only.lower().split()
        words = [word for word in words]
        yield words


def sentence_to_words_sl(doc):
    for sentence in to_sentences(doc):
        letters_only = pattern.sub(' ', sentence)
        words = letters_only.lower().split()
        words = [word for word in words if word not in stopwords]
        yield words
