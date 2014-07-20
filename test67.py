#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
import math
def cos_similarity(word1,word2,data):
	vector1=defaultdict(lambda :0)
	vector2=defaultdict(lambda :0)

	keys=[]
	for line in open(data): #noun_context_vector
		line = line.strip().split("\t")
		
		if line[0] == word1:
			for phrase_freq in line[1:]:
				phrase_freq=phrase_freq.split(":")
				if len(phrase_freq) > 2:
					phrase_freq[0]=":".join(phrase_freq[:2])
					phrase_freq[1]=phrase_freq[-1]
				#print phrase_freq
				keys.append(phrase_freq[0])
				vector1[phrase_freq[0]]=float(phrase_freq[1])

		elif line[0] == word2:
			for phrase_freq in line[1:]:
				#print phrase_freq
				phrase_freq=phrase_freq.split(":")
				if len(phrase_freq) > 2:
					phrase_freq[0]=":".join(phrase_freq[:2])
					phrase_freq[1]=phrase_freq[-1]
				#print phrase_freq
				keys.append(phrase_freq[0])
				vector2[phrase_freq[0]]=float(phrase_freq[1])
				
		else:pass

	cos_similarity=0
	#print keys
	for word in set(keys):
		"""
		print "kakesan"
		print vector1[word]
		print vector2[word]
		"""
		cos_similarity += vector1[word] *vector2[word]
	return cos_similarity

if __name__ == "__main__":
	print cos_similarity("ハンター","モンスター",sys.argv[1])