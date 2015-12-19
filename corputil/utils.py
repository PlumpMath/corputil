import nltk


def get_tokenizer(lang):
    model = 'tokenizers/punkt/{}.pickle'.format(lang.lower())
    return nltk.data.load(model)
