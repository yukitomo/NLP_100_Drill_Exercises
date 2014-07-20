#!/usr/bin/python
#-*-coding:utf-8-*-

col2=[]
from collections import Counter

for line in open("col2.txt","r"):
	col2.append(line)

counter = Counter(col2)

for word, cnt in counter.most_common():
	print word,

print counter.most_common(10)