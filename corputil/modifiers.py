import re
from .utils import get_tokenizer, get_stopwords


pattern = re.compile(r'[\W\d]')


def sentences(doc, lang):
    tokenizer = get_tokenizer(lang)
    raw_sentences = tokenizer.tokenize(doc.strip())
    for sentence in raw_sentences:
        yield sentence


def sentences_token(doc, lang, stopwords):
    stopwords = get_stopwords(stopwords)
    for sentence in sentences(doc, lang):
        letters_only = pattern.sub(' ', sentence)
        words = letters_only.lower().split()
        words = [word for word in words
                 if word not in stopwords and len(word) > 1]
        yield words


def doc_token(doc, stopwords):
    stopwords = get_stopwords(stopwords)
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words
             if word not in stopwords and len(word) > 1]
    yield words


def doc_sentences_token(doc, lang, stopwords):
    sentence_list = list(sentences_token(doc, lang, stopwords))
    yield sentence_list
