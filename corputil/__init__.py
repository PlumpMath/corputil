class Corpus(object):
    def __init__(self, filename, modifier=None, encoding='UTF-8'):
        self.filename = filename
        self.modifier = modifier
        self.encoding = encoding

    def __iter__(self):
        for doc in open(self.filename, encoding=self.encoding):
            if self.modifier:
                yield from self.modifier(doc)
            else:
                yield doc


class MultiCorpus(object):
    def __init__(self, filenames, modifier=None, encoding='UTF-8'):
        self.filenames = filenames
        self.modifier = modifier
        self.encoding = encoding

    def __iter__(self):
        for filename in self.filenames:
            corpus = Corpus(filename, modifier=self.modifier, encoding=self.encoding)
            yield from corpus
