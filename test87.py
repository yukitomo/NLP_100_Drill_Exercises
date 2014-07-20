#!/usr/bin/python
#-*-coding:utf-8-*-
import pymongo
from pymongo import *
import json
import sys


con = Connection('localhost')
#コネクションからtestデータベースを取得
db = con.nlp100_tomo
#testデータベースからfooコレクションを取得
col = db.tweets
top_count = col.find({"freq_rted":{"$gt":0}}).sort("freq_rted",pymongo.DESCENDING)
for data in top_count:
	print data

