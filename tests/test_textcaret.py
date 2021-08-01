from textcaret import __version__
from textcaret import TextCaret,TextSentiment


def test_version():
    assert __version__ == '0.0.1'

def test_isTextCaret():
    pass 


def test_isTextSentiment():
    pass 

def test_TextCaret_sentiment_report():
    s = "I love apples. John hates eating onions without using a mint afterwards"
    docx = TextCaret(s)
    results = docx.sentiment_report()
    results_as_sentence = results['sentence']
    results_as_sentiment = results['sentiment'].polarity
    # {'sentence': 'I love apples. John hates eating onions without using a mint afterwards', 'sentiment': Sentiment(polarity=0.5, subjectivity=0.6)}   
    assert results_as_sentiment == 0.5
    assert type(results_as_sentence) == str

def test_TextCaret_summary_report():
    s = "I love apples. John hates eating onions without using a mint afterwards"
    docx = TextCaret(s)
    results = docx.summary_report()
    assert type(results) == dict

def test_TextCaret_visual_report():
    s = "I love apples. John hates eating onions without using a mint afterwards"
    docx = TextCaret(s)
    results = docx.visual_report()
    assert type(results) != None
