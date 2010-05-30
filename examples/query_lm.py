#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from pynlpl.lm.lm import SimpleLanguageModel

#syntax: ./query_lm.py lm_file sentence

lmfile = sys.argv[1]

lm = SimpleLanguageModel()
lm.load(lmfile)
print lm.scoresentence(sys.argv[2:])