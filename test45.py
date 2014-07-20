#!/user/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
from test41 import mecab_input

data_japanese=sys.argv[1]
text=mecab_input(data_japanese)


#test45:AのBという表現を抜き出せ
for m in range(len(text)):
	for n in range(len(text[m])):
		if text[m][n]["surface"]=="の":
			if text[m][n-1]["pos"]=="名詞" and text[m][n+1]["pos"]=="名詞":
				print text[m][n-1]["surface"]+text[m][n]["surface"]+text[m][n+1]["surface"]+"\n",
			else:pass
		else:pass

