#!/user/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab

#data_japanese=sys.argv[1]

#text=[sentence1,sentence2,.....]
#sentence=[morpheme1,morpheme2,....]
#morpheme={"surface":表層系,"base":基本形,"pos":品詞,"pos1":品詞細分類１}
#text[m][n]["surface"]

def mecab_input(data):
	text=[]
	for line in open(data):
		tagger = MeCab.Tagger("mecabrc")
		sent=tagger.parse(line).strip() #一文まるごとの解析データ
		words=sent.split("\n")
		sentence=[]
		for word in words:
			if not word=="EOS":
				word_items=word.split("\t")
				word_items2=word_items[1].split(",")
				morpheme={"surface":word_items[0],"base":word_items2[6],"pos":word_items2[0],"pos1":word_items2[1]}
				sentence.append(morpheme)
			else:
				pass
		text.append(sentence)
	return text

#text=mecab_input(data_japanese)








