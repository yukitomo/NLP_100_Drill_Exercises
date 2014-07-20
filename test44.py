#!/user/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
from test41 import mecab_input

data_japanese=sys.argv[1]
text=mecab_input(data_japanese)


#test44:サ変名詞を出力
for m in range(len(text)):
	for n in range(len(text[m])):
		if text[m][n]["pos"]=="名詞" and text[m][n]["pos1"]=="サ変接続":
			print text[m][n]["surface"]+"\t"+text[m][n]["base"]+"\n",

"""
>>> print m.parse("(掃除)")
(	名詞,サ変接続,*,*,*,*,*
掃除	名詞,サ変接続,*,*,*,*,掃除,ソウジ,ソージ
)	名詞,サ変接続,*,*,*,*,*
"""