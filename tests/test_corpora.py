from corputil import FileCorpus, MultiFileCorpus
from os import path

test_file1 = path.join('tests', 'data', 'corpus_1.txt')
test_file2 = path.join('tests', 'data', 'corpus_2.txt')


def test_corpus():
    corpus = FileCorpus(test_file1)
    corpora = [doc for doc in corpus]
    assert len(corpora) is 4


def test_multicorpus():
    corpus = MultiFileCorpus([test_file1, test_file2])
    corpora = [doc for doc in corpus]
    assert len(corpora) is 10
