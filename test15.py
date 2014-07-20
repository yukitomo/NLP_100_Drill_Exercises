#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'(@)([a-zA-Z0-9_]{1,}?)(?=:)')


for line in open(sys.argv[1]):
	match=pattern.search(line)
	if match:
		url='<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>'
		dst = url.replace('xxxxxxx',match.group(2))
		print dst