#!/usr/bin/python
#-*-coding:utf-8-*-
#(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#確認 bash test2.sh

f=open('address.txt','r')

for line in f:
	print line.replace("\t"," ").strip()

