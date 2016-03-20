#########################################################################
#-*- coding:utf-8 -*-
# File Name: rewho.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月20日 星期日 21时51分16秒
#########################################################################
#!/usr/bin/env python2.7

from re import split
from os import popen

f = popen('who','r')
for eachline in f:
	print split('\s\s+|\t',eachline.strip())#slpit by '\s\s+\t'
f.close()

