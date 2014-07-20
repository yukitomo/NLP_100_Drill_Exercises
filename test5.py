#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
n= int( sys.argv[2])

print n

f=open(sys.argv[1],"r")

for i in range(n):
	print f.readline(),

