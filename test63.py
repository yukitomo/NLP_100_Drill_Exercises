#!/usr/bin/python
#-*-coding:utf-8-*-

#text63:62の結果を用い，それぞれの名詞句のTF*IDF値を計算し，"(名詞句)\t(TF*IDF値)\t(TF値)\t(DF値)"の形式で出力せよ．
#ある名詞句wがあるとき，freq(w)をコーパス全体での名詞句wの出現頻度，df(w)を名詞句wが出現するファイルの数，Nを総ファイル数とし，TF*IDF値は freq(w) * log(N / df(w)) として計算せよ

import sys
from collections import defaultdict
import os, os.path
from test53 import *
import math
work = 'work'

def input_dir_txt_n(dir): #ディレクトリ中のファイル.nのパスのリストを返す
	for root,dirs,files in os.walk(dir):
		#print root,dirs,files
		paths=[]
		for file in files:
			file_address = os.path.join(root, file)
			if file_address[-2:] == ".n":
				#print file_address
				paths.append(file_address)
		return paths

if __name__ == "__main__":
	df=defaultdict(lambda :[])
	tf=defaultdict(lambda :0)
	readfiles=input_dir_txt_n(work) #.nのつくファイルのパスのリスト
	N=len(readfiles)
	#print readfiles
	for readfile in readfiles:
		for nounphrase in open(readfile,"r"):
			nounphrase=nounphrase.strip()
			tf[nounphrase] += 1 #名詞句のコーパス中の総合出現回数
			if not readfile in df[nounphrase]:
				df[nounphrase].append(readfile)

	for k in df:
		TF=tf[k]
		DF=len(df[k])
		TFIDF=float(TF)*math.log(float(N)/DF,2)
		print k+"\t"+str(TFIDF)+"\t"+str(TF)+"\t"+str(DF)




