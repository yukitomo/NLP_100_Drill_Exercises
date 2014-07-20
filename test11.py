#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'拡散希望')

for line in open(sys.argv[1]):
	if pattern.search(line):
		print line.strip()

