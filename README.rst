textcaret
=========

Simplified NLP Toolkit for common NLP Tasks

Why TextCaret
-------------

Installation
------------

textcaret is available on pypi hence you can install using pip

.. code:: bash

   pip install textcaret

Usage
-----

.. code:: python

   >>> from textcaret import TextCaret,TextSummarizer,TextSentiment
   >>> docx = TextCaret(text='your text goes here')

Perform TextSummarization
-------------------------

.. code:: python

   >>> from textcaret import TextSummarizer
   >>> s = "your text"
   >>> summarizer = TextSummarizer(s)
   >>> summarizer.summarize()

Perform Sentiment Analysis
--------------------------

.. code:: python

   >>> from textcaret import TextSentiment
   >>> docx = TextSentiment("I love coding and teaching.John hates mangoes so bad he doesn't eat it")
   >>> 
   >>> docx.sentiment()
   {'sentence': "I love coding and teaching.John hates mangoes so bad he doesn't eat it", 'sentiment': Sentiment(polarity=-0.09999999999999992, subjectivity=0.6333333333333333)}
   >>> 
   >>> docx.sentiment()['sentiment']
   Sentiment(polarity=-0.09999999999999992, subjectivity=0.6333333333333333)
   >>> 
   >>> docx.sentiment()['sentiment'].polarity
   -0.09999999999999992
   >>> 
   >>> docx.sentiment()['sentiment'].subjectivity
   0.6333333333333333
   >>> 

Perform Sentiment on Splitted/Tokenized Sentences
-------------------------------------------------

.. code:: python

   >>> docx.split_sentence=True
   >>> 
   >>> docx.sentiment()
   {'sentiment': [('I love coding and teaching', 0.5), ("John hates mangoes so bad he doesn't eat it", -0.6999999999999998)]}
   >>> 
