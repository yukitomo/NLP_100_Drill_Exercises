#!/usr/bin/python
#-*-coding:utf-8-*-
#(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ

import sys
n= int(sys.argv[1])
f=open("address.txt","r")

for i in range(n):
	print f.readline(),

