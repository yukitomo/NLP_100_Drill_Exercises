#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re 

noun_tfidf={}
pattern=re.compile(r'[0-9:^]')

for line in open(sys.argv[1]):
	items=line.strip().split("\t") #名詞句,TF*IDF,TF,DF
	noun_tfidf[items[0]]=float(items[1])

i=0
for k,v in sorted(noun_tfidf.items(), key=lambda x:x[1], reverse=True):
	if not pattern.search(k) : #数字の無い表現
		if i < 100:
			print str(i)+"\t"+k+"\t"+str(v)
		i += 1
