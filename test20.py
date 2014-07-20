#!/usr/bin/python
#-*-coding:utf-8-*-
import sys 
import re

pattern = re.compile(r'\([^一-額ぁ-んァ-ヴ]{3,6}\)')
pattern1 = re.compile(r'\([^0-9]{3,6}\)')
pattern2 = re.compile(r'\([^0a-zA-Z]{3,6}\)')

for line in open(sys.argv[1]):
	match = pattern.search(line)
	if pattern.search(line) :
		print match.group(0)