#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

trainfile=open(sys.argv[1],"r")
sent=[]

for line in trainfile:
	line=line.strip()
	if not line == "":
		sent.append(line)
		if line == ".":
			for i in range(1,len(sent)):
				bi = "\t".join(sent[i-1:i+1])
				print bi
			sent=[]






