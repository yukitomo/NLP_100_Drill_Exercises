#!/usr/bin/python
#-*-coding:utf-8-*-

#test61:コーパスディレクトリ中の各ファイルに対して，cabochaを適用し，適当なディレクトリに係り受け解析の結果を格納せよ．
"""
cabocha -f1 ./corpus/japanese_2.txt > ./work/ja_2_cabocha.txt
"""
#test62:61で作成した各ファイルから，名詞句（文節中の名詞の連接）を抜き出して，個別のファイルに格納せよ．

import sys
from collections import defaultdict
import os, os.path
from test53 import *
work = 'work'

def input_dir_txt(dir): #ディレクトリ中のファイルのパスのリストを返す
	for root,dirs,files in os.walk(dir):
		#print root,dirs,files
		paths=[]
		for file in files:
			file_address = os.path.join(root, file)
			if file_address[-3:] == "txt":
				#print file_address
				paths.append(file_address)
		return paths

if __name__ == "__main__":
	for readfile in input_dir_txt(work):
		print readfile
		writefile=open(readfile+".n","w") #書き込みファイル名
		text=cabocha_input_chunk(readfile) #chunkに格納
		for i in range(len(text)): #はセンテンスの番号
			for j in range(len(text[i])): #はchunkの番号
				phrases=text[i][j].show_noun_phrase_in() 
				for k in range(len(phrases)):
					#print phrases[k]
					writefile.write(phrases[k].strip()+"\n")






