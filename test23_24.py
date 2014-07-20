#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re


sents=open(sys.argv[1])
pattern = re.compile(r'[,?!.]$')

for line in sents:
	words = line.split(' ')
	for word in words:
		m = pattern.search(word)
		if m:
			print word[:m.start()]
			print word[m.start()]
		else:
			print word
	print ""