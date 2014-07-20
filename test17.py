#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

pattern = re.compile(u'([一-龠]{2,5})(さん|氏|ちゃん)')


for line in open(sys.argv[1]):
	line = line.decode("utf-8")
	match=pattern.search(line)
	if match:
		print match.group(0).encode("utf-8")