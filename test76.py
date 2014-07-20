#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import os, os.path
from test72 import *

def make_NPlearning_data(readfile,morph_text): #各テキスト
	writefile=open(readfile[:-9]+"geniaf.txt","w")
	NPs = input_NP_text(morph_text) #NPsに各NPを格納
	for NP in NPs:
		writefile.write(NP.showinfo(),)
		#print NP.showinfo(),
			

if __name__ == "__main__":
	for readfile in input_dir_genia("set8"):
		#print readfile
		morph_text = input_morph_txt(readfile)
		make_NPlearning_data(readfile, morph_text)

#77 学習 classias-train -tn -m model.txt  english.geniaf.txt english_2.geniaf.txt english_3.geniaf.txt english_4.geniaf.txt english_5.geniaf.txt
#78 cat english.geniaf.txt | classias-tag -m model.txt -r
#79 5分割交差検定 classias-train -tn -g5 -x english.geniaf.txt english_2.geniaf.txt english_3.geniaf.txt english_4.geniaf.txt english_5.geniaf.txt