# This project crawls a webpage to create a dictionary of words vs their frequencies.
# The final outcome is a histogram of the top 15 words.

import requests
from bs4 import BeautifulSoup
import string
from nltk.corpus import words as words_in_nltk
import operator
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')
    for post_text in soup.find_all('div', {'class':'post-bodycopy cf'}):
        content = post_text.string
        words = content.lower().split()
        for word in words:
            word_list.append(word)
    clean_up_list(word_list)  # To remove non-word characters


def clean_up_list(word_list):
    cleaned_word_list = []
    for word in word_list:
        for char in string.punctuation:
            word = word.replace(char, '')
        if word in words_in_nltk.words():  # Only valid words(236,736) from NLTK are appended
            cleaned_word_list.append(word)
    create_dictionary(cleaned_word_list)


def create_dictionary(word_list):
    word_dict = {}
    top_fifteen_words = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    for k, v in sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True):
        if len(top_fifteen_words) >= 15:
            break
        else:
            top_fifteen_words[k] = v

    create_histogram(top_fifteen_words)


def create_histogram(dictionary_content):
    counts = Counter(dictionary_content)

    labels, values = zip(*counts.items())

    labels = np.array(labels)
    values = np.array(values)

    indexes = np.arange(len(labels))

    bar_width = 0.35
    plt.bar(indexes, values)
    plt.xticks(indexes + bar_width, labels, fontsize=9, rotation='vertical')
    plt.title('A Histogram of Top 15 words', {'fontsize': 15})
    plt.show()

start('https://www.pythonforbeginners.com/')