#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

class Morph:
	def __init__(self,surface,base,pos,pos1): #morphe=Morphe(surface,base,pos,pos1)
		#print '[Morph.__init__]'
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1
	
	def showinfo(self):
		#print '[Morph.showinfo]'
		print  "[surface,base,pos,pos1] = ["+self.surface+","+self.base+","+self.pos+","+self.pos1+"]"

class Chunk:
	def __init__(self,morphs,dst,srcs): #chunk=Chunk(morphs,dst,src) dst:係り先文節インデックス番号 srcs:係り元文節インデックスリスト
		#print '[Chunk.__init__]'
		self.morphs=morphs
		self.dst=dst
		self.srcs=srcs
	def showinfo2(self):
		#print '[Chunk.showinfo]'
		for k in range(len(self.morphs)):
			print self.morphs[k].showinfo()
		print "dst=", self.dst, "srcs=", self.srcs

	
"""
--------------ja_caboha.txt--------------------       |
* 0 1D 0/1 0.000000                                   |chunk0 dst=1,srcs=[]
本編	名詞,一般,*,*,*,*,本編,ホンペン,ホンペン              | morph0
の	助詞,連体化,*,*,*,*,の,ノ,ノ                        | morph1 

* 1 -1D 3/3 0.000000                                   |chunk1 dst=None,srcs=[1]
主人公	名詞,一般,*,*,*,*,主人公,シュジンコウ,シュジンコー  |morph0
[	名詞,サ変接続,*,*,*,*,*                              |morph1
編集	名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー
]	名詞,サ変接続,*,*,*,*,*
EOS
"""

def cabocha_input_sent(data):
	text=[] #text=[sent0,sent1,sent2,......]
	sent=[] #sent=[morph0,morph1,morph2,....] 1文が入っている
	for line in open(data): #ja_caboha.txt, short_ja_cabocha.txt
		line = line.strip()
		if not line[:2] == "* " and not line == "EOS":
			word_items=line.split("\t") # word_items=["表層系","名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー"]
			word_items2=word_items[1].split(",")
			morph = Morph(word_items[0],word_items2[6],word_items2[0],word_items2[1])
			sent.append(morph)
		elif line == "EOS":	
			text.append(sent)
			sent=[]
		else:pass
	return text

def cabocha_input_chunk(data):
	text=[] #=[sent0,sent1.....]
	sent=[] #=[chunk0,chunk1,......] 1文節が入っている
	srcs_dict=defaultdict(lambda :[]) #={0:[],1:[0],....,ID:[3,4..]}
	morphs=[]
	for line in open(data): #ja_caboha.txt, short_ja_cabocha.txt
		line = line.strip()
		if line[:2] == "* ":
			if len(morphs) != 0:
				chunk=Chunk(morphs,dst,srcs)
				sent.append(chunk)
				srcs_dict[ID]=[]	
			morphs=[]
			info=line.strip().split()
			ID=int(info[1]) #chunkのID
			dst=int(info[2][:-1]) #Dの除去
			srcs_dict[dst].append(ID) #係り先のdstをキーとして、係りもととしてIDの値をアペンド
			srcs=srcs_dict[ID]
		elif not line == "EOS":
			word_items=line.split("\t") # word_items=["表層系","名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー"]
			word_items2=word_items[1].split(",")
			morph = Morph(word_items[0],word_items2[6],word_items2[0],word_items2[1])
			morphs.append(morph)
		elif line == "EOS":	
			text.append(sent)
			sent=[]
		else:pass
	chunk=Chunk(morphs,dst,srcs)
	sent.append(chunk)	
	text.append(sent)	
	return text


if __name__ == "__main__":
	
	data=sys.argv[1] #ja_caboha.txt, short_ja_cabocha.txt
	text = cabocha_input_sent(sys.argv[1]) #テキスト格納
		
	for i in range(len(text)): 
		for j in range(len(text[i])):
			text[i][j].showinfo()
			if j == len(text[i])-1:
				print ""
	


