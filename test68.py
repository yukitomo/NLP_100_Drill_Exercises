#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
import math
from test67 import *
import itertools

words=[] 
for line in open(sys.argv[1]): #noun_context_vector
	line = line.strip().split("\t")
	words.append(line[0])
words=set(words)

top_smilarity={}
for t in list(itertools.combinations(words,2)): #各フレーズの組み合わせ
	#print t
	similarity=cos_similarity(t[0],t[1],sys.argv[1])
	if similarity >= 0.6:
		top_smilarity[t[0]+"\t"+t[1]]=similarity
		
for k,v in sorted(top_smilarity.items(),key=lambda x:x[1],reverse=True):
	print str(v)+"\t"+k