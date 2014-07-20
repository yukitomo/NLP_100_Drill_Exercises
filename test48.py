#!/user/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict

count=defaultdict(lambda: 0)

for line in open(sys.argv[1]):
	count[line.strip()] += 1

for k, v in sorted(count.items(), key=lambda x:x[1], reverse=True):
	print k+" "+str(v)