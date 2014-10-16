#!/usr/bin/python
#-*-coding:utf-8-*-
#(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

f=open('address.txt','r')

for line in f:
	print line.replace("\t"," ").strip()

