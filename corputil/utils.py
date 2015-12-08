import os
import nltk
import pkgutil


def get_stopwords(lang):
    if not lang:
        return frozenset()
    if isinstance(lang, list):
        return frozenset(lang)
    path = os.path.join('stopwords', '{}.txt'.format(lang))
    try:
        stopwords = pkgutil.get_data('corputil', path)
    except IOError:
        raise ValueError('Stopwords for language {} is missing'.format(lang))
    return frozenset(word.decode('UTF-8') for word in stopwords.splitlines())


def get_tokenizer(lang):
    model = 'tokenizers/punkt/{}.pickle'.format(lang.lower())
    return nltk.data.load(model)
