#!/usr/bin/python
#-*-coding:utf-8-*-
import pymongo
from pymongo import *
import json
import sys
import re

if __name__ == '__main__':
	con = Connection('localhost')
	#コネクションからtestデータベースを取得
	db = con.nlp100_tomo
	#testデータベースからfooコレクションを取得
	col = db.tweets2
	query = sys.argv[1]

	for data in col.find({"body":re.compile(query)}).sort("freq_rted",pymongo.DESCENDING):
		print data["body"]
		