#!/Users/shang/anaconda/bin/python
#!-*-coding:utf-8-*-
# File Name: reducer.py
# Author: by sql
# Created Time: 二  9/20 17:50:38 2016
# Description: 
#***************************************

import sys

last_id, last_num = None,0
for line in sys.stdin:
	uId, uNum = line.strip().split('\t')
	if last_id and last_id != uId:
		print "%s\t%s" % (last_id, last_num)
		last_id, last_num = uId, int(uNum)
	else:
		last_id, last_num = (uId, last_num + int(uNum))

if last_id:
	print "%s\t%s" % (last_id, last_num)

