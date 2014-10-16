#!/usr/bin/python
#-*-coding:utf-8-*-
#(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．

import sys
itemList=[]

for line in open(sys.argv[1]):
	itemList.append(line.strip())

print len(set(itemList))
