#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal

dicttionary_marshall = open(sys.argv[1])
test = open(sys.argv[2])

dictionary = marshal.load(dicttionary_marshall)

for line in test:
	count = 0
	words=line.split("\t")
	word=words[2]
	if word in dictionary.keys():
		count += 1
	if count > 2:
		print word + " : " + str(dictionary[words[1]]) 