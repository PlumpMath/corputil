import re
import nltk

from .utils import get_stopwords


tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
stopwords = get_stopwords('german')
pattern = re.compile(r'[\W\d]')


def to_words(doc):
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words if len(word) > 1]
    yield words


def to_words_sl(doc):
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words
             if word not in stopwords and len(word) > 1]
    yield words


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
        words = [word for word in words
                 if word not in stopwords and len(word) > 1]
        yield words
