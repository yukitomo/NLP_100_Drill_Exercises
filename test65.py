	#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
import os, os.path
from test53 import *
from test62 import *
import math
import re

noun_phrases=[] #top100の名詞句を格納
for noun_phrase in open(sys.argv[1]): #top100tfidf
	noun_phrase=noun_phrase.strip().split("\t")
	noun_phrases.append(noun_phrase[1])

for readfile in input_dir_txt(work):
		#print readfile
		text=cabocha_input_chunk(readfile) #chunkに格納
		for i in range(len(text)): #はセンテンスの番号
			for j in range(len(text[i])): #はchunkの番号
				for noun_phrase in noun_phrases: #top100の各名詞句
					pattern = re.compile(noun_phrase) 
					chunk_phrase=text[i][j].show_phrase()
					if pattern.search(chunk_phrase):
						#print noun_phrase
						#print chunk_phrase
						dst=text[i][j].dst
						srcs=text[i][j].srcs
						words_dst=None #事前にNoneを与え、dst=-1のものだけNoneになるようにする
						words_src=None
						if not dst == -1 :
							words_dst=text[i][dst].show_noun_verb_adjective() #係り先周辺単語のリスト
							#print words_dst
						else:pass
						if not words_dst==None:
							for word in words_dst:
								print noun_phrase+"\t->\t"+word
						if not srcs == []:
							for src in srcs:
								words_src=text[i][src].show_noun_verb_adjective()
								if not words_src==None:
									for word in words_src:
										print noun_phrase+"\t<- "+word
						else:pass