#!/user/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
from test41 import mecab_input

data_japanese=sys.argv[1]
text=mecab_input(data_japanese)
mylist=[]

#test46:文章中のすべての名詞の連接（１形態素以上）を抜き出せ．
mylist=[]
for m in range(len(text)):
	for n in range(len(text[m])):
		if text[m][n]["pos"]=="名詞":
			mylist.append(text[m][n]["surface"])
			n += 1
		elif len(mylist)>0:
			print " ".join(mylist)+"\n",
			mylist=[]
		else:pass
			