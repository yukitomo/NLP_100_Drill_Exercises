#!/user/bin/python
#-*-coding:utf-8-*-
#(13)非公式RTのツイートの中で，RT先へのコメント部分のみを抽出せよ．
#python test13.py tweets.txt 

import sys
import re

pattern1 = re.compile(r'(:)( ?)(\S+)( ?)(?=RT @)')

for line in open(sys.argv[1]):
	match=pattern1.search(line)
	if match:
		print match.group(3)
		print line