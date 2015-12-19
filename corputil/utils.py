import nltk


def get_stopwords(sw):
    if not sw:
        sw = []
    return frozenset(sw)


def get_tokenizer(lang):
    model = 'tokenizers/punkt/{}.pickle'.format(lang.lower())
    return nltk.data.load(model)
