#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
from test53 import *

f=open("test60.dot", "w")

f.write('digraph "g" {\n')

for line in open(sys.argv[1]):
	items=line.strip().split('\t')
	#print items
	if len(items) > 1:
		f.write('\t"'+items[0]+'" -> "'+items[1]+'" ;\n')

f.write('}')

#neato -Tsvg test60.dot