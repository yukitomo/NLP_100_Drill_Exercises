#!/usr/bin/python
#-*-coding:utf-8-*-
#(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．
#cut -f 2 address.txt|sort | uniq -c | sort -k 1 -r > test10_2.result

from collections import defaultdict

col2 = defaultdict(int)
for line in open("col2.txt","r"):
	col2[line.strip()] += 1  

for k,v in sorted(col2.items(),key=lambda x:x[1], reverse = True):
	print k ,v
