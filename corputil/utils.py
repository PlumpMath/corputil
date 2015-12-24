import nltk


def finalize_stopwords(sw):
    if not sw:
        sw = []
    return frozenset(sw)


def init_tokenizer(lang):
    model = 'tokenizers/punkt/{}.pickle'.format(lang.lower())
    return nltk.data.load(model)


def load_stopwords(file_path, encoding='UTF-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        stopwords = f.read().split('\n')[:-1]
    if stopwords:
        return stopwords
    else:
        return []
