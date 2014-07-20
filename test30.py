#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re
import string
from stemming.porter2 import stem

words=open(sys.argv[1])

for line in words:
	word = line[:-1].split('	')
	word_stem = stem(word[1])
	linedash = word[0]+"	"+word[1]+"	"+word_stem
	print linedash