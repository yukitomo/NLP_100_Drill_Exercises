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
	for j in range(len(text_chunk[i])): #はchunkの番号
		srcs=text_chunk[i][j].srcs
		if len(srcs) > 1:
			phrase_be_done=text_chunk[i][j].show_phrase()
			phrase_do_s=[]
			for src in srcs:
				phrase_do=text_chunk[i][src].show_phrase()
				phrase_do_s.append(phrase_do)
			print "--係り元の文節--"
			for phrase in phrase_do_s:
				print phrase
			print "--係り先の文節--"			
			print phrase_be_done
			print ""




		











		