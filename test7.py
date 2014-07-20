#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
itemList=[]

for line in open(sys.argv[1]):
	itemList.append(line)

print len(set(itemList))
