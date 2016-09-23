#!/Users/shang/anaconda/bin/python
#!-*-coding:utf-8-*-
# File Name: mapper.py
# Author: by sql
# Created Time: 二  9/20 17:48:37 2016
# Description: 
#***************************************


import sys

for line in sys.stdin:
	val = line.strip().split('\t')
	uId = val[0];
	uNum = val[1];
	print "%s\t%s" % (uId, uNum)


