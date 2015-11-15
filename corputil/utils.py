import os
import pkgutil


def get_stopwords(lang):
    path = os.path.join('stopwords', '{}.txt'.format(lang))
    try:
        stopwords = pkgutil.get_data('corputil', path)
    except IOError:
        raise ValueError('Stopwords for language {} is missing'.format(lang))
    return frozenset(word.decode('UTF-8') for word in stopwords.splitlines())


