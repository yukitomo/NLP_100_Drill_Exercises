#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal

dicttionary_marshall = open(sys.argv[1])
test = open(sys.argv[2])

dictionary = marshal.load(dicttionary_marshall)

for line in test:
	words=line.split("\t")
	word=words[1]
	if not word in dictionary.keys():
		print word 