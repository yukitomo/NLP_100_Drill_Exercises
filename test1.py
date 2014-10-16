#!/usr/bin/python
#-*-coding:utf-8-*-
#(1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．
#確認 bash test1.sh

a = 0
f=open('address.txt','r')

for line in f:
	a += 1

print a