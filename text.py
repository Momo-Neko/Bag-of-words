# coding: utf-8
import sys
import os
import pickle
import numpy as np
from janome.tokenizer import Tokenizer

def Text_Data(file):

    # ファイルの読み込み
    f = open(file)
    text = f.read()
    f.close()
    text = text.split('\n')

    # 文章で分割
    for i in range(len(text)):
        text[i] = text[i].split('。')

    # 以下形態素解析（形態素に分割）

    # 格納準備
    t = Tokenizer()
    new_text = []
    word_list = []

    # 日付削除しない場合
    for i in range(len(text)):
        new_text = new_text + text[i]
    print(new_text)

    # トークナイズして，リストに格納
    for j in range(len(new_text)):
        tokens = t.tokenize(new_text[j])
        for k in range(len(tokens)):
            word_list.append(tokens[k].surface)

    # 除去する要素を指定 ＝ 除去リスト
    rems = ['@', ',', '，', '。', ' ', 'http', 'https','//', '、', '×', '.',
            '+', '＋', 
            '/',', ', '(', ')', '（', '）', '://', 'RT', ':', ';','：', '；',
            '」','「', '＠', '-', '／',  '%', '％', '!', '！', '#', '＃',
            '$', '＄', '=', '＝', 'ー', '￥', '^', '{', '}', '~', '～', 
            '&', '＆', '・', '?', '??', '？', '？？',  '<', '＜', '>', '＞', '_', '＿', 
            'co', 'jp', '(@', '○', '『', '』', '”', '’', '"', '…', 
            ')」', '〇', '【', '】', '[', ']', '', '', '', '', '', '', '', '', '', 

            'から', 'より', 'こそ', 'でも', 'しか','さえ', 'けれど', 'たり', 'つつ', 'とも',
            'たら', 'ある', 'なら', 'のに', 'です', 'ます', 'する', 'ほど', 'ない', 'くる',
            'なり', 'そう', 'まし', 'その', 'この', 'あの', 'せる', 'どう', 'ため', 'どこ',
            'いる', 'これ', 'それ', 'あれ', 'いい', 'など', 'あっ', 'もう', 'さん', 'じゃ',
            'から', 'あり', 'ので', 'とも', 'ませ', 'でし', 'とき', 'こと', 'なる', 'って',
            'ただ', 'まで', 'もの', 'つか', 'なっ', 'でき', 'もっ', 'けど', 'ほぼ', 'なー',
            'そこ', 'ここ', 'だろ', 'なん', 'だっ', 'なあ', 'っけ', 'せる', 'やっ', 'また',
            '', '', '', '',

            'どれ', 'なれ', 'かも', 'いく', 'いけ', 'いう', 'たい', 'あと', 'かも', 'しれ',  
            'こう', 'なく', 'よく', 'だけ', 'れる', 'よう', 'かけ', 'どの', 'てる', 'とか',
            'という', '思う', '思っ', 'として', 'ところ', 'しまう', 'なんか', 'そんな', 
            'でしょ', 'しまい', 'わかり', 'まま', '', '', '', '', ''
            ]

    # 除去リストに数字を追加 
    for number in range(10000):
        rems.append(str(number))

    # 除去リストに追加 ― 一文字のひらがなとカタカナ，全角数字，アルファベット大文字・小文字
    hirakana    = [chr(i) for i in range(12353, 12436)]
    katakana    = [chr(i) for i in range(12449, 12533)]
    zenkaku_num = [chr(i) for i in range(65296, 65296+10)]
    alph_L      = [chr(i) for i in range(97, 97+26)]
    alph_S      = [chr(i) for i in range(65, 65+26)]
    for a in range(len(hirakana)):
        rems.append(hirakana[a])
    for b in range(len(katakana)):
        rems.append(katakana[b])
    for c in range(len(zenkaku_num)):
        rems.append(zenkaku_num[c])
    for d in range(len(alph_L)):
        rems.append(alph_L[d])
    for e in range(len(alph_S)):
        rems.append(alph_S[e])

    words = [x for x in word_list if (x in rems) == False]

    return words

