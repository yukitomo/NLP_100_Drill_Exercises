#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
import math

words_vector=defaultdict(lambda :defaultdict(lambda :0))

for line in open(sys.argv[1]): #noun_dependency
	line=line.strip().split("\t")
	if line[1] != "->" and line[1] != "<-":
		words_vector[line[0]][line[1]] += 1
	else:
		pass
		#print line[1]

for word,vector in words_vector.items():
	total_square=0
	for count in vector.values():
		total_square += count**2
	length=math.sqrt(total_square) 
	for element,count in vector.items():
		words_vector[word][element] = float(count) / length

for word,vector in words_vector.items():
	print word+"\t", #普通にプリントすると最後に改行が付加されてしまうため,をつける
	for element,value in vector.items():
		print element+":"+str(value)+"\t",
	print ""
	

