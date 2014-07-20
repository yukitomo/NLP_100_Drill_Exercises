#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from collections import defaultdict

data=[]
word_count=defaultdict(lambda: 0)
for line in open(sys.argv[1]):
	items=line.strip().split()
	word_count[items[0]]=int(items[1])
	data.append(int(items[1]))

print data

plt.hist(data,bins=100,range=(0,50))
plt.show()


"""
freq_type=defaultdict(lambda: 0) #{頻度:異なり数,....}
for v in word_count.values():
	freq_type[v] += 1
#print word_count
x=[]
y=[]
for k, v in sorted(freq_type.items(), key=lambda x:x[1], reverse=True):
	#print str(k)+" "+str(v)
	x.append(k)
	y.append(v)
fig, axes = plt.subplots(figsize=(7,4)) 
axes.plot(x, y, 'r')
axes.set_xlabel('frequent') #x軸のラベルを設定します
axes.set_ylabel('type') #y軸のラベルを設定します
axes.set_title('title') #titleを設定します
fig.savefig("freq_type.png") #これで画像を保存. オプション引数でdpiも指定できますよ！
fig.show()

"""
p=[]
q=[]
order=1
for k,v in sorted(word_count.items(), key=lambda x:x[1], reverse=True):
	p.append(order)
	q.append(v)
	order += 1
fig2, axes2 = plt.subplots(figsize=(7,4)) 
axes2.plot(p, q, 'r')
axes2.set_xlabel('order') #x軸のラベルを設定します
axes2.set_ylabel('frequent') #y軸のラベルを設定します
axes2.set_title('title') #titleを設定します
fig2.savefig("order_freq.png") #これで画像を保存. オプション引数でdpiも指定できますよ！
plt.show()


