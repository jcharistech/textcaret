textcaret
=========

Simplified NLP Toolkit for common NLP Tasks

Why TextCaret
-------------

-  The problem: performing common NLP Task such as
   summarization,sentiment analysis,etc are essential however you may
   need to use different libraries and write different codes for
   performing the same set of task on different texts
-  The goal of TextCaret is to simplify this task by providing a unified
   framework to perform these common NLP Tasks

Installation
------------

textcaret is available on pypi hence you can install using pip

.. code:: bash

   pip install textcaret

Usage
-----

.. code:: python

   >>> import textcaret as tc 
   >>> docx = tc.TextCaret(text='your text goes here')
   >>>
   >>> docx.visual_report()
   >>> docx.summary_report()
   >>> docx.sentiment_report()
   >>> docx.general_report()

Perform Text Visualization For Insights
---------------------------------------

-  This generates wordcloud plots,token and tags frequency plots, word
   length distribution and more.

.. code:: python

   >>> from textcaret import TextViz
   >>> s = "your text"
   >>> viz = TextViz(s)
   >>> viz.visualize()
   >>> # Save Plot
   >>> viz.safe_figure('mynewplot.png')

Perform TextSummarization
-------------------------

-  In NLP Text Summarization is the process of shortening a set of data
   computationally, to create a subset (a summary) that represents the
   most important or relevant information within the original
   content.[wiki]
-  It is the process of finding the most informative sentence in a
   document.
-  TextCaret uses several extractive algorithms for generating summary

.. code:: python

   >>> from textcaret import TextSummarizer
   >>> s = "your text"
   >>> summarizer = TextSummarizer(s)
   >>> summarizer.summarize()

Perform Sentiment Analysis
--------------------------

-  In NLP, Sentiment Analysis is the process of identifying the
   emotions/sentiment or feeling in a given text either as
   positive,negative or neutral.
-  It is a form of text classification
-  TextCaret uses the famous textblob library behind the scene to
   generate sentiments of given text

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

Dependencies
------------

Textcaret is built ontop of powerful and common NLP libraries such as
below + NLTK + TextBlob + Sumy + Neattext + Matplotlib + Wordcloud +
Spacy

.
-

-  Maintainer: Jesse E.Agbe(JCharis)
-  Jesus Saves @JCharisTech

Contributions
-------------

-  Notice a bug, please let us know
-  We appreciate contributions of anykind.
-  Happy Coding!!! :smiley:
