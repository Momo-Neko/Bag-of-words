# coding: utf-8
import os
import glob
import numpy as np
from text import Text_Data
from NLP_func import *
import pandas as pd

# 1. テキストファイル読み込み
words = Text_Data("kokoro.txt")
print(words)

# 2. id へ変換
word_to_id = {}
id_to_word = {}
word_to_id, id_to_word = id_preprocess(words, word_to_id, id_to_word)

print("2. word_to_id:")
print(word_to_id)
print("2. id_to_word:")
print(id_to_word)

# 3. コーパスの作成と格納
corpus_dic = {}
corpus_dic = corpus_preprocess(words, word_to_id, id_to_word)
print("3. corpus_dic:")
print(corpus_dic)

# 4. Bag of Words (BOW) 作成
bag_of_words = {}
vocab_size = len(word_to_id) # = len(id_to_word) 

bag_of_words = {}
corpus_size = len(corpus_dic)
for i in range(vocab_size):
    count = 0
    for j in range(corpus_size):
        if corpus_dic[j] == i:
            count += 1
    bag_of_words[id_to_word[i]] = count

bag_of_words = sorted(bag_of_words.items(), key = lambda x: x[1], reverse=True)
print("4. bag_of_words:")
print(bag_of_words)

# 5. 単語を ID 順に CSV ファイルへ保存  # BOW を CSV ファイルへ保存
Table = pd.DataFrame(bag_of_words)
Table.to_csv('Table.csv', index=False, encoding="shift_jis")


