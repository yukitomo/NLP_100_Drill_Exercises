#! /usr/bin/env python
# -*- python -*-
# -*- encoding: utf-8 -*-
 
import sys
import re
 
for line in sys.stdin.readline().split("."):
    print re.match("\.\s[A-Z]",line)