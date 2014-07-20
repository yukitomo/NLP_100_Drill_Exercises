#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
a = 0
f1=open('col1.txt','w')
f2=open('col2.txt','w')

for line in open(sys.argv[1]):
	a+=1
	line2=line.replace("	"," ")
	print line2,
	itemList = line2[:-1].split(' ')
	#print itemList[1]
	f1.write(itemList[0]+"\n")
	f2.write(itemList[1]+"\n")
	
print a
#print sys.argv[0]
#print sys.argv[1]


f1.close()
f2.close()


