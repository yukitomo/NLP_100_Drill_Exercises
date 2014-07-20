#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
training_file=open(sys.argv[1],"r")

context_counts=defaultdict(lambda: 0)

for line in training_file:
	context_counts[line] += 1

for key,value in context_counts.items():
	print str(value)+"\t"+key,