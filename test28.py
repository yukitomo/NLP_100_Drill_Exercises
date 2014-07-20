#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re
import string

bigram=[]
from collections import Counter
#pattern = re.compile(r'[\s.,]')

for line in open(sys.argv[1]):
	line=line.lower().strip().translate(string.maketrans("", ""), ",.()")
	if line != "":
		for a in range(len(line)-1):
			bi=line[a:a+2]
			bigram.append(bi)

counter = Counter(bigram)

for bi, cnt in counter.most_common(100):
	print bi+" : "+str(cnt)

#print counter.most_common(100)

"""
dictionary={}
for word, cnt in counter.most_common():
	dictionary[word]=cnt
"""


