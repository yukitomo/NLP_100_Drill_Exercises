#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
n= int(sys.argv[2])

print n

f=open(sys.argv[1],"r")
itemList=[]

for line in f:
	itemList.append(line)

for k in range(n):
	print itemList[len(itemList)-n+k],

