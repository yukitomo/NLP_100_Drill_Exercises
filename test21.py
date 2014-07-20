#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

text = open(sys.argv[1])


for line in text:
	sents = line.split('.')
	for sent in sents:
		sent=sent.strip()+"." #stripを入れないと文頭に空白文字が入ってしまう
		if sent != ".":
			print sent