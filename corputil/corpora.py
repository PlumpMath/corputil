from .modifiers import sentences, sentences_token, doc_sentences_token, doc_token


class FileCorpus(object):
    def __init__(self, *args, encoding='UTF-8'):
        self.files = [file for file in args]
        self.encoding = encoding

    def __iter__(self):
        for file in self.files:
            for doc in open(file, encoding=self.encoding):
                yield doc

    def doc_token(self, stopwords=None):
        for doc in self:
            yield from doc_token(doc, stopwords)

    def doc_sentences_token(self, lang='german', stopwords=None):
        for doc in self:
            yield from doc_sentences_token(doc, lang, stopwords)

    def sentences(self, lang='german'):
        for doc in self:
            yield from sentences(doc, lang)

    def sentences_token(self, lang='german', stopwords=None):
        for doc in self:
            yield from sentences_token(doc, lang, stopwords)


class StreamCorpus(object):
    def __init__(self, *args):
        self.streams = [stream for stream in args]

    def __iter__(self):
        for stream in self.streams:
            for doc in stream:
                yield doc

    def doc_token(self, stopwords=None):
        for doc in self:
            yield from doc_token(doc, stopwords)

    def doc_sentences_token(self, lang='german', stopwords=None):
        for doc in self:
            yield from doc_sentences_token(doc, lang, stopwords)

    def sentences(self, lang='german'):
        for doc in self:
            yield from sentences(doc, lang)

    def sentences_token(self, lang='german', stopwords=None):
        for doc in self:
            yield from sentences_token(doc, lang, stopwords)
