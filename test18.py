#!/usr/bin/python
#-*-coding:utf-8-*-
import sys 
import re

pattern = re.compile(u'(仙台市)([^\s\w\d　]{1,20}[\d０-９〇一-九十上下東西]+)*')

for line in open(sys.argv[1]):
	line = line.decode("utf-8")
	match=pattern.search(line)
	if match:
		print match.group(0).encode("utf-8")