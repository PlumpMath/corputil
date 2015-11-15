class FileCorpus(object):
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


class MultiFileCorpus(object):
    def __init__(self, filenames, modifier=None, encoding='UTF-8'):
        self.filenames = filenames
        self.modifier = modifier
        self.encoding = encoding

    def __iter__(self):
        for filename in self.filenames:
            corpus = FileCorpus(filename, modifier=self.modifier, encoding=self.encoding)
            yield from corpus


class StreamCorpus(object):
    def __init__(self, stream, modifier=None):
        self.stream = stream
        self.modifier = modifier

    def __iter__(self):
        for doc in self.stream:
            if self.modifier:
                yield from self.modifier(doc)
            else:
                yield doc


class MultiStreamCorpus(object):
    def __init__(self, streams, modifier=None):
        self.streams = streams
        self.modifier = modifier

    def __iter__(self):
        for stream in self.streams:
            corpus = StreamCorpus(stream, modifier=self.modifier)
            yield from corpus
