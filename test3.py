#!/usr/bin/python
#-*-coding:utf-8-*-
#(3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

a = 0
f1=open('col1.txt','w')
f2=open('col2.txt','w')

for line in open('address.txt','r'):
	itemList = line.strip().split('\t')
	#print itemList[0], itemList[1]
	if len(itemList) == 1 :
		itemList.append(" ") 
	f1.write(itemList[0]+"\n")
	f2.write(itemList[1]+"\n")

f1.close()
f2.close()


