#!/user/bin/python
#-*-coding:utf-8-*-

import MeCab
from test41 import mecab_input
import optparse
parser = optparse.OptionParser()

parser.add_option('-t','--text') #テキストファイルのアドレス
parser.add_option('-v','--verb',action='store_true')
parser.add_option('-b','--verb_base',action='store_true')
parser.add_option('-s','--sahen_noun',action='store_true')
parser.add_option('-n','--noun_no_noun',action='store_true')
parser.add_option('-p','--linked_noun',action='store_true')
options, args = parser.parse_args()

#print args
text=mecab_input(options.text)

#test42:動詞を抜き出す
if options.verb :
	for m in range(len(text)):
		for n in range(len(text[m])):		
			if text[m][n]["pos"]=="動詞":
				print text[m][n]["surface"]+"\n",

#test43:動詞の基本形を出力 
if options.verb_base:
	for m in range(len(text)):
		for n in range(len(text[m])):		
			if text[m][n]["pos"]=="動詞":
				print text[m][n]["base"]+"\n",

#test44:サ変名詞を出力
if options.sahen_noun:
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["pos"]=="名詞" and text[m][n]["pos1"]=="サ変接続":
				print text[m][n]["surface"]+"\t"+text[m][n]["base"]+"\n",

#test45:AのBという表現を抜き出せ
if options.noun_no_noun:
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["surface"]=="の":
				if text[m][n-1]["pos"]=="名詞" and text[m][n+1]["pos"]=="名詞":
					print text[m][n-1]["surface"]+text[m][n]["surface"]+text[m][n+1]["surface"]+"\n",
				else:pass
			else:pass

#test46:文章中のすべての名詞の連接（１形態素以上）を抜き出せ．
if options.linked_noun:
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

