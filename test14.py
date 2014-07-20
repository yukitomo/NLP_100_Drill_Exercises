#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'(@)([a-zA-Z0-9_]{1,}?)(?=:)')


for line in open(sys.argv[1]):
	match=pattern.search(line)
	if match:
		print match.group(2)
