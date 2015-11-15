from corputil import FileCorpus
from corputil.modifiers import to_sentences, to_words, to_words_sl
from os import path


test_file2 = path.join('tests', 'data', 'test_corpus_2.txt')


def test_without():
    pass


def test_words_sl():
    wordlist = [
        ['damen', 'herren'],
        ['führt', 'institut'],
        ['spd', 'vorgeschlagenen', 'dezentralen', 'einreisezentren', 'bessere', 'konzept'],
        ['richtigen', 'schritte', 'getan'],
        ['einhergehenden', 'üppigeren', 'spritverbrauch', 'geld', 'ausgleichen', 'fahrer', 'autos', 'zugehen'],
        ['thema', 'mitte', 'gesellschaft', 'angekommen']
    ]
    corpus = FileCorpus(test_file2, modifier=to_words_sl)
    for i, words in enumerate(corpus):
        if i is 0:
            print(words)
            assert words == wordlist[i]


def test_sentences():
    sentencelist = [
        'Hallo meine Damen und Herren.', 'Wie geht es Ihnen heute?', 'Er führt das Institut seit 2008.',
        'Die von der SPD vorgeschlagenen dezentralen Einreisezentren seien das bessere Konzept.',
        'Aber dafür müssen jetzt auch die richtigen Schritte getan werden.',
        'Er muss auch den damit einhergehenden üppigeren Spritverbrauch mit Geld ausgleichen.',
        'Und er muss auch auf die Fahrer der mehrere Millionen Autos zugehen.',
        'Es zeigt ja auch, dass das Thema in der Mitte der Gesellschaft angekommen ist.'
    ]
    corpus = FileCorpus(test_file2, modifier=to_sentences)
    for i, sentence in enumerate(corpus):
        print(sentence)
        assert sentence == sentencelist[i]
