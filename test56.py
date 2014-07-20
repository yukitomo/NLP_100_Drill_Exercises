#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
from test53 import *


#test55:係り元の文節と係り先の文節をタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

data=sys.argv[1] #ja_caboha.txt, short_ja_cabocha.txt
#morphe=Morphe(surface,base,pos,pos1)
text_chunk = cabocha_input_chunk(sys.argv[1]) 
#text_chunk=[sent0,sent1,sent2,.....]
#sent=[chunk0,chunk1,chunk2,....]
#chunk=Chunk(morphs=[morph0,morph1,morph2,...],dst,srcs=[0,5,...])


#print "text_len=",len(text_chunk)
#print text_chunk
for i in range(len(text_chunk)): #はセンテンスの番号
	#print "sent_len",len(text_chunk[i])
	#print text_chunk[i]
	for j in range(len(text_chunk[i])): #はchunkの番号
		#print i,j
		if text_chunk[i][j].noun_in(): #chunkが名詞をもつか
			"""
			for k in range(len(text_chunk[i][j].morphs)):
				text_chunk[i][j].morphs[k].showinfo()
			"""
			word_do=text_chunk[i][j].show_phrase()
			dst=text_chunk[i][j].dst
			word_be_done="None" #事前にNoneを与え、dst=-1のものだけNoneになるようにする
			if not dst == -1 :
				if text_chunk[i][dst].verb_in():
					#print text_chunk[i][dst].verb_in()
					"""
					for k in range(len(text_chunk[i][dst].morphs)):
						text_chunk[i][dst].morphs[k].showinfo()
					"""
					word_be_done=text_chunk[i][dst].show_phrase()
					#print word_be_done
					if not word_be_done=="None":
						#print i,j
						dependency = word_do+"\t"+word_be_done
						print dependency
						#print dependency.translate(string.maketrans("",""),"。、")
