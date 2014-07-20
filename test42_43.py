#!/user/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
from test41 import mecab_input

data_japanese=sys.argv[1]
text=mecab_input(data_japanese)


#test42:動詞を抜き出す
#test43:動詞の基本形を出力 
for m in range(len(text)):
	for n in range(len(text[m])):
		if text[m][n]["pos"]=="動詞":
			print text[m][n]["surface"]+"\t"+text[m][n]["base"]+"\n",
