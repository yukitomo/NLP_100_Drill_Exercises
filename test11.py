#!/usr/bin/python
#-*-coding:utf-8-*-
#(11) 「拡散希望」という文字列を含むツイートを抽出せよ．
#cat tweets.txt | grep 拡散希望| wc -l
#python test11.py tweets.txt | wc -l

import sys
import re

pattern = re.compile(r'拡散希望')

for line in open(sys.argv[1]):
	if pattern.search(line):
		print line.strip()

