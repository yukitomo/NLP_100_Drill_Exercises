#!/usr/bin/python
#-*-coding:utf-8-*-
from pymongo import Connection
import json
import sys


con = Connection('localhost')
#コネクションからtestデータベースを取得
db = con.nlp100_tomo
#testデータベースからfooコレクションを取得
col = db.tweets

search_url = sys.argv[1] #特定のURL
for data in col.find({"url":search_url}):
	print data

