#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal

text = open(sys.argv[1])
#dictionary=defaultdict(lambda: 0) #defaultdictで定義するとmarshall.dumpでエラーになる
dictionary={}
datafile=open('dictionary.txt', 'wb')

for line in text:
	boxes = line.split('|')
	if boxes[0] in dictionary.keys()
		dictionary[boxes[0]]=(boxes[1],boxes[3],boxes[6])
	else:
		dictionary[boxes[0]]

	

#print "Input search_word"
#word=raw_input()
#print dictionary[word]

marshal.dump(dictionary,datafile)
