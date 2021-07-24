from collections import Counter,defaultdict
import matplotlib.pyplot as plt 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
import random


def get_most_common_tokens(docx,num=10):
	word_freq = Counter(docx.split())
	most_common_tokens = word_freq.most_common(num)
	return dict(most_common_tokens)


def plot_wordcloud(docx):
	mywordcloud = WordCloud().generate(docx)
	plt.imshow(mywordcloud,interpolation='bilinear')
	plt.axis('off')
	st.pyplot()


def plot_mendelhall_curve(docx):
	word_length = [ len(token) for token in docx.split()]
	word_length_count = Counter(word_length)
	sorted_word_length_count = sorted(dict(word_length_count).items())
	x,y = zip(*sorted_word_length_count)
	fig = plt.figure(figsize=(20,10))
	plt.plot(x,y)
	plt.title("Plot of Word Length Distribution")
	plt.show()
	st.pyplot(fig)

def visualize_text(docx):
	"""Visualize Text Supplied
	
	Returns: several plots such as wordcloud,mendelhall_curve,pos_tags plot etc
	"""
	pass


def summarize_text(docx,num_sentence=2):
	"""Summarize Text
	
	Returns: a summary of text as either textrank or lexrank extractive form of summary
	"""
	# For Strings
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	# Using LexRank
	summarizer_lex = LexRankSummarizer()
	summarizer_luhn = LuhnSummarizer()
	summarizer_lsa = LsaSummarizer()

	# Summarize Docs
	summary_for_lex =summarizer_lex(parser.document,num_sentence)
	summary_for_luhn =summarizer_luhn(parser.document,num_sentence)
	summary_for_lsa =summarizer_lsa(parser.document,num_sentence)

	# Results
	summary_results = {'lexrank':summary_for_lex,'luhn':summary_for_luhn,'lsa':summary_for_lsa}

	return summary_results
		

def analyze_text(docx):
	"""Analyze Text lexically

	"""
	pass


# Source https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/5-Text-Generation.ipynb
def markov_chain(text):
    """Returns a dictionary with each word as
    a key and each value as the list of words that come after the key in the text."""

    # Tokenize the text by word, though including punctuation
    words = text.split(" ")

    # Initialize a default dictionary to hold all of the words and next words
    m_dict = defaultdict(list)

    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    m_dict = dict(m_dict)
    return m_dict


def __generate_text(chain, count=15):
    """Input a dictionary in the format of key = current word, value = list of next words
    along with the number of words you would like to see in your generated sentence."""

    # Capitalize the first word
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count - 1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += " " + word2

    # End it with a period
    sentence += "."
    # print(sentence)
    return sentence


def generate_text(text, num_of_words=15):
    """Returns a new sentence/text From a given text using Markov Chains
    Parameters
    ----------
    text : Main Text
    num_of_words : number of words to generate
    Returns
    ----------
    Returns a new sentence of the number of words specified
    Usage
    ------
    >>> from textcaret.functions import generate_text
    >>> t1 = "your text...here"
    >>> generate_text(t1)
    >>> generate_text(t1,20)
    #Alternatively generate 4 sentences
    >>> for i in range(4):
            print(generate_text(t1,15))
    """
    result_dict = markov_chain(text)
    final_result_sentence = __generate_text(result_dict, num_of_words)
    return final_result_sentence

