#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
from test53 import *

f=open("test69.dot", "w")

f.write('graph "g" {\n')

for line in open(sys.argv[1]):
	items=line.strip().split('\t')

	#print items
	if len(items) > 1:
		f.write('\t"'+items[1]+'" -- "'+items[2]+'" ;\n')

f.write('}')

#neato -Tsvg test69.dot