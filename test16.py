#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'([一-龠]+)(\([A-Z]+\))')
#pattern = re.compile(r'\([A-Z]+?\)')

for line in open(sys.argv[1]):
	match=pattern.search(line)
	if match:
		print match.group(1)+"	"+match.group(2)
