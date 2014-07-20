#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re
import string

words=[]
from collections import Counter
#pattern = re.compile(r'[\s.,]')

for line in open(sys.argv[1]):
	line=line.lower().strip().translate(string.maketrans("", ""), ",.()")
	if line != "":
		words.append(line)

counter = Counter(words)


for word, cnt in counter.most_common(100):
	print word+" : "+str(cnt)

"""
dictionary={}
for word, cnt in counter.most_common():
	dictionary[word]=cnt
"""


