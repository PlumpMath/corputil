from corputil import FileCorpus
from os import path


test_file2 = path.join('tests', 'data', 'corpus_2.txt')


def test_sentences_token():
    wordlist = [
        ['damen', 'herren'],
        [],
        ['führt', 'institut'],
        ['vorgeschlagenen', 'dezentralen', 'einreisezentren', 'bessere', 'konzept'],
        ['richtigen', 'schritte'],
        ['einhergehenden', 'üppigeren', 'spritverbrauch', 'geld', 'ausgleichen'],
        ['fahrer', 'autos', 'zugehen'],
        ['mitte', 'gesellschaft', 'angekommen']
    ]
    corpus = FileCorpus(test_file2).sentences_token(stopwords='german')
    assert all(this == that for this, that in zip(corpus, wordlist))


def test_sentences():
    sentencelist = [
        'Hallo meine Damen und Herren.', 'Wie geht es Ihnen heute?', 'Er führt das Institut seit 2008.',
        'Die von der SPD vorgeschlagenen dezentralen Einreisezentren seien das bessere Konzept.',
        'Aber dafür müssen jetzt auch die richtigen Schritte getan werden.',
        'Er muss auch den damit einhergehenden üppigeren Spritverbrauch mit Geld ausgleichen.',
        'Und er muss auch auf die Fahrer der mehrere Millionen Autos zugehen.',
        'Es zeigt ja auch, dass das Thema in der Mitte der Gesellschaft angekommen ist.'
    ]
    corpus = FileCorpus(test_file2).sentences()
    assert all(this == that for this, that in zip(corpus, sentencelist))

