#!/usr/bin/python
#-*-coding:utf-8-*-

f=open("col1col2.txt","w")

itemList1=[]
itemList2=[]

import sys
for line in open(sys.argv[1]):
	itemList1.append(line[:-1])

for line in open(sys.argv[2]):
	itemList2.append(line)

        
for k in range(len(itemList1)):
	f.write(itemList1[k]+"	"+itemList2[k])
f.close()

for k in range(len(itemList1)):
    print itemList1[k]+"	"+itemList2[k],
