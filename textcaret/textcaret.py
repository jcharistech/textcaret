# -*- coding: utf-8 -*-
# This file is part of the NEAT Project suite of libraries
# Please see the LICENSE file that should have been included as part of this
# package.

from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from textblob import TextBlob
from textcaret.functions import visualize_text,save_visualized_text


class TextViz(object):
    """docstring for TextViz

    Usage::
    >>> from textcaret import TextViz
    >>> docx = " your text document "
    >>> tv = TextViz(docx)
    >>> tv.visualize()

    """

    def __init__(self, text=None):
        super(TextViz, self).__init__()
        self.text = text

    def __repr__(self):
        return "TextViz(text='{}')".format(self.text)

    def __str__(self):
        return self.text

    def plot_most_common_tokens(self, num=10):
        word_freq = Counter(self.text.split())
        most_common_tokens = word_freq.most_common(num)
        x, y = zip(*most_common_tokens)
        fig = plt.figure(figsize=(20, 10))
        plt.bar(x, y)
        plt.title("Most Common Tokens")
        plt.xticks(rotation=45)
        plt.show()

    def plot_wordcloud(self):
        mywordcloud = WordCloud().generate(self.text)
        plt.imshow(mywordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show(block=True)

    def plot_mendelhall_curve(self):
        word_length = [len(token) for token in self.text.split()]
        word_length_count = Counter(word_length)
        sorted_word_length_count = sorted(dict(word_length_count).items())
        x, y = zip(*sorted_word_length_count)
        fig = plt.figure(figsize=(20, 10))
        plt.plot(x, y)
        plt.title("Plot of Word Length Distribution")
        plt.show()

    def visualize(self):
        return visualize_text(self.text)

    def save_figure(self,filename):
        """Save Plot or Figure
        
        usage:
        >>> vis.save_figure('myplot.png')

        """
        return save_visualized_text(self.text,filename)


class TextSummarizer(object):
    """TextSummarizer: summarize a given document/text using several summarization
    algorithms such as lexrank,luhn,lsa,etc

    Returns: A Dictionary of various summary per the each extractive algorithm

    Usage::
    >>> from textcaret import TextSummarizer
    >>> s = "your text"
    >>> summarizer = TextSummarizer(s)
    >>> summarizer.summarize()
    >>> # Number of Sentence Summary to Generate
    >>> summarizer.summarize(num_sentence=3)

    """

    def __init__(self, text=None):
        super(TextSummarizer, self).__init__()
        self.text = text

    def __repr__(self):
        return "TextSummarizer(text='{}')".format(self.text)

    def __str__(self):
        return self.text

    def summarize(self, num_sentence=2):
        docx = self.text
        # For Strings
        parser = PlaintextParser.from_string(docx, Tokenizer("english"))
        # Using LexRank
        summarizer_lex = LexRankSummarizer()
        summarizer_luhn = LuhnSummarizer()
        summarizer_lsa = LsaSummarizer()

        # Summarize Docs
        summary_for_lex = summarizer_lex(parser.document, num_sentence)
        summary_for_luhn = summarizer_luhn(parser.document, num_sentence)
        summary_for_lsa = summarizer_lsa(parser.document, num_sentence)

        # Results
        summary_results = {
            "lexrank": summary_for_lex,
            "luhn": summary_for_luhn,
            "lsa": summary_for_lsa,
        }

        return summary_results


class TextSentiment(object):
    """docstring for TextSentiment"""

    def __init__(self, text=None, split_sentence=False):
        super(TextSentiment, self).__init__()
        self.text = text
        self.split_sentence = False

    def __repr__(self):
        return 'TextSentiment(text="{}",split_sentence="{}")'.format(
            self.text, self.split_sentence
        )

    def __str__(self):
        return self.text

    def sentiment(self):
        if self.split_sentence == True:
            sentence_tokens = [sent for sent in str(self.text).split(".")]
            sentiment_list = []
            for sent in sentence_tokens:
                sentiment = TextBlob(sent).sentiment
                results = (sent, sentiment.polarity)
                sentiment_list.append(results)
            sentiment_results = {"sentiment": sentiment_list}
        else:
            blob = TextBlob(self.text)
            sentiment = blob.sentiment
            sentiment_results = {"sentence": self.text, "sentiment": sentiment}
        return sentiment_results


class TextCaret(TextViz, TextSummarizer, TextSentiment):
    """TextCaret: main object for nlp task

    Returns: TextCaret Object

    Usage::
    >>> from textcaret import TextCaret
    >>> s = "your text"
    >>> docx = TextCaret(s)
    >>> docx.visual_report()
    >>> docx.summary_report()
    >>> docx.sentiment_report()
    >>> docx.general_report()

    """

    def __init__(self, text=None):
        super(TextCaret, self).__init__()
        self.text = text

    def __repr__(self):
        return "TextCaret(text='{}')".format(self.text)

    def __str__(self):
        return self.text

    def prepare(self, stopwords=False, special_char=False, punctuations=False):
        import neattext.functions as nfx

        if stopwords == True:
            self.text = nfx.remove_stopwords(self.text)
        if special_char == True:
            self.text = nfx.remove_special_characters(self.text)
        else:
            self.text = self.text

        prepared_text = self.text
        return prepared_text

    def visual_report(self):
        """Visualize The Given Text
        Generate a visual report of several plot for the given text


        """
        new_docx = TextViz(self.text)
        # Generate Plots
        return new_docx.visualize()

    def summary_report(self,num_sentence=2):
        """Summarize the Given Text
        Generate a summary report of the given text

        Usage::
        >>> docx = TextCaret("your text here")
        >>> docx.summary_report()
        >>>
        >>> docx.summary_report(num_sentence=1)

        """
        new_docx = TextSummarizer(self.text)
        # Generate Summary
        return new_docx.summarize(num_sentence)

    def sentiment_report(self):
        """Perform Sentiment Analysis on Text
        Generate a sentiment report of the given text

        Usage::
        >>> docx = TextCaret("your text here")
        >>> docx.sentiment_report()
        >>>  
        """

        new_docx = TextSentiment(self.text,split_sentence=True)
        # Generate Sentiment Report
        return new_docx.sentiment()

    def general_report(self):
        """Generate A General Report of the Analysis of the Text

        Usage:
        >>> docx = TextCaret("your text here")
        >>> docx.general_report()

        """
        import neattext as nt
        docx = nt.TextFrame(self.text)
        return docx.describe()