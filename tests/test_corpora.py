from corputil import Corpus, MultiCorpus
from os import path

test_file1 = path.join('tests', 'data', 'test_corpus_1.txt')
test_file2 = path.join('tests', 'data', 'test_corpus_2.txt')


def test_corpus():
    corpus = Corpus(test_file1)
    corpora = []
    for doc in corpus:
        corpora.append(doc)
    assert len(corpora) is 4


def test_multicorpus():
    corpus = MultiCorpus([test_file1, test_file2])
    corpora = []
    for doc in corpus:
        corpora.append(doc)
    assert len(corpora) is 10
