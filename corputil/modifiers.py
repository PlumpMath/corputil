import re
from .utils import init_tokenizer, finalize_stopwords


pattern = re.compile(r'[\W\d]')


def sentences(doc, lang):
    tokenizer = init_tokenizer(lang)
    raw_sentences = tokenizer.tokenize(doc.strip())
    for sentence in raw_sentences:
        yield sentence


def sentences_token(doc, lang, stopwords):
    stopwords = finalize_stopwords(stopwords)
    for sentence in sentences(doc, lang):
        letters_only = pattern.sub(' ', sentence)
        words = letters_only.lower().split()
        words = [word for word in words
                 if word not in stopwords and len(word) > 1]
        yield words


def doc_token(doc, stopwords):
    stopwords = finalize_stopwords(stopwords)
    letters_only = pattern.sub(' ', doc)
    words = letters_only.lower().split()
    words = [word for word in words
             if word not in stopwords and len(word) > 1]
    yield words


def doc_sentences_token(doc, lang, stopwords):
    sentence_list = list(sentences_token(doc, lang, stopwords))
    yield sentence_list
