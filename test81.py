#!/usr/bin/python
#-*-coding:utf-8-*-
from pymongo import Connection
import json
import sys

f = open(sys.argv[1])
data = json.load(f)

#コネクション作成
con = Connection('localhost')
#コネクションからtestデータベースを取得
db = con.nlp100_tomo
#testデータベースからfooコレクションを取得
col = db.tweets

for i in data:
	#print i
	url = "https://twitter.com/"+i["user"]["screen_name"]+"/status/"+str(i["id"])
	#print i["in_reply_to_screen_name"],"in_reply_to_screen_name"
	#print i["in_reply_to_status_id"],"in_reply_to_status_id"
	if i["in_reply_to_screen_name"] is None:
		reply_url = None	
	else:
		reply_url = "https://twitter.com/"+i["in_reply_to_screen_name"]+"/status/"+str(i["in_reply_to_status_id"])
	input_data = {"url":url, \
	"date":i["created_at"],\
	"user":i["user"]["screen_name"],\
	"nickname":i["user"]["name"],\
	"body":i["text"],\
	"reply_url":reply_url,\
	"freq_rted":int(i["retweet_count"])\
	}
	col.insert(input_data)