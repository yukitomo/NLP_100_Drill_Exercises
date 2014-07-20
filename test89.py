#!/usr/bin/python
#-*-coding:utf-8-*-
import pymongo
from pymongo import *
import json
import sys

if __name__ == '__main__':
	con = Connection('localhost')
	#コネクションからtestデータベースを取得
	db = con.nlp100_tomo
	#testデータベースからfooコレクションを取得
	col = db.tweets2

	for data in col.find({"bigram":"記憶"}):
		print data["body"]
		