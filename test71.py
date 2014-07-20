#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
import os, os.path
from test62 import *
from geniatagger import *
import re 
#https://pypi.python.org/pypi/geniatagger-python/0.1

tagger = GeniaTagger('/Users/yukitomo/geniatagger-3.0.1/geniatagger')
pattern = re.compile(r'(\.\s[A-Z])|(\.\[[0-9]+\]\s[A-Z])')

if __name__ == "__main__":
	for readfile in input_dir_txt("set8"):
		print readfile
		writefile=open(readfile+".genia","w") #書き込みファイル名 

		for line in open(readfile): #各テキストファイルの改行ごと
			if line.strip() != "":
				start = 0 #検索開始のインデックス
				while len(line) > start: #文字列の長さよりインデックスは小さくなければならない
					m = pattern.search(line,start)
					if m:
						sent = line[start:m.start()+1]
						start = m.end()-1
					else:
						sent = line[start:].strip()
						break
					#print tagger.parse(line)
					#print sent
					
					for item in tagger.parse(sent): #[('This', 'This', 'DT', 'B-NP', 'O'), ('is', 'be', 'VBZ', 'B-VP', 'O'), ('a', 'a', 'DT', 'B-NP', 'O'), ('pen', 'pen', 'NN', 'I-NP', 'O'), ('.', '.', '.', 'O', 'O')]
						writefile.write("\t".join(item)+"\n") #形態素解析したものを書き込み
						#print "\t".join(item)
					writefile.write("EOS"+"\n")
					#print "EOS"
					