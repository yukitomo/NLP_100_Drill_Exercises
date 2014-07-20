#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
trainfile=open(sys.argv[1],"r")
trainfile2=open(sys.argv[1],"r")
#trainfile = of.read()
sent=[]
unigram=defaultdict(lambda :0)

print trainfile

for line in trainfile:
	bigram=line.strip().split("\t")
	unigram[bigram[1]] += 1 #ある単語wの回数を数える。

for line in trainfile2:
	bigram=line.strip().split("\t")
	probability=float(bigram[0])/unigram[bigram[1]]
	print str(probability)+"\t"+bigram[1]+"\t"+bigram[2]




