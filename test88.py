#!/usr/bin/python
#-*-coding:utf-8-*-
import pymongo
from pymongo import *
import json
import sys

def bigram_list(text): #textはユニコード
	bigram = []
	for i in range(len(text)-1):
		bigram.append(text[i:i+2])
	return bigram

if __name__ == '__main__':
	con = Connection('localhost')
	#コネクションからtestデータベースを取得
	db = con.nlp100_tomo
	#testデータベースからfooコレクションを取得
	col = db.tweets

	for data in col.find():
		#print data["body"]
		bigram = bigram_list(data["body"])
		#for bi in bigram:
		#	print bi
		col.update({"_id":data["_id"]},{"$set":{"bigram":bigram}})

		
