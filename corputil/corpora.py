from .modifiers import sentences, sentences_token, doc_sentences_token, doc_token


class Corpus(object):
    def __iter__(self):
        pass

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


class FileCorpus(Corpus):
    def __init__(self, files, encoding='UTF-8'):
        self.files = files
        self.encoding = encoding

    def __iter__(self):
        for file in self.files:
            for doc in open(file, encoding=self.encoding):
                yield doc


class StreamCorpus(Corpus):
    def __init__(self, streams):
        self.streams = streams

    def __iter__(self):
        for stream in self.streams:
            for doc in stream:
                yield doc


class ListCorpus(Corpus):
    def __init__(self, l):
        self.list = l

    def __iter__(self):
        for doc in self.list:
            yield doc
