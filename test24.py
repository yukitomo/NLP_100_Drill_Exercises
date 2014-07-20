#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

tokens = open(sys.argv[1])

for token in tokens:
	print token.strip()+"	"+token.lower()