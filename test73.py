#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import os, os.path
from test72 import *

if __name__ == "__main__":
	NP=[]
	texts = input_morph_dir("set8")
	for text in texts: #各テキスト
		for sent in text: #各文
			for morph in sent: #各morph
				if morph.chunk == "B-NP" : #名詞句のはじまり
					if NP != []:
						print "#"+" ".join(NP)
						NP=[]
					NP.append(morph.surface)
				elif morph.chunk == "I-NP": #名詞句の中間
					NP.append(morph.surface)
				else:
					if NP != []:
						print "#"+" ".join(NP)
						NP=[]

