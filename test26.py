#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

tokens = open(sys.argv[1])
pattern = re.compile(r'(ly|ness)$')

for line in tokens:
	if pattern.search(line):
		print line.strip()