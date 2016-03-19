#########################################################################
#-*- coding:utf-8 -*-
# File Name: max_line.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月19日 星期六 20时15分57秒
#########################################################################
#!/usr/bin/env python2.7
import os

def max_line():
	f = open('./qqq.txt','r')
	longest = max(len(x.strip()) for x in f)# 生成器
	f.close()
	return longest
