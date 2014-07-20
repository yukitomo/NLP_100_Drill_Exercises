#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(r'([一-龠]+)(さん|氏|ちゃん)')


for line in open(sys.argv[1]):
	match=pattern.search(line)
	if match:
		print match.group(2)
