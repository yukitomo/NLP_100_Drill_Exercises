#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import os, os.path
from test72 import *

if __name__ == "__main__":
	for readfile in input_dir_genia("set8"): #各geniaファイルのアドレスを取得
		#print readfile
		morph_text = input_morph_txt(readfile) #geniaファイルからmorphのリストを作成
		NPs = input_NP_text(morph_text) #morphのリストから名詞句のリストを作成
		for NP in NPs:
			print NP.showinfo(),