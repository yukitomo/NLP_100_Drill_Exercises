#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'なう$')

for line in open(sys.argv[1]):
	if pattern.search(line):
		print line.strip()