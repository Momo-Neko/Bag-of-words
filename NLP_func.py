# coding: utf-8
import numpy as np

def id_preprocess(words, word_to_id, id_to_word):
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    return word_to_id, id_to_word

def corpus_preprocess(words, word_to_id, id_to_word):
    corpus = np.array([word_to_id[w] for w in words])
    return corpus
