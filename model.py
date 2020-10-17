import markovify
import string
import numpy as np
from collections import defaultdict


def markov_chain(text):
    m_dict = defaultdict(list)
    for current_word, next_word in zip(text[0:-1], text[1:]):
        m_dict[current_word].append(next_word)
    m_dict = dict(m_dict)
    return m_dict

def prepare_text():
    with open('винник.txt', encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table).lower() for w in words]
    word_dict = markov_chain(stripped)
    return word_dict

def generate_sentence(chain=prepare_text(), count=12):
    word1 = np.random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    for i in range(count-1):
        word2 = np.random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    sentence += '.'
    return(sentence)

