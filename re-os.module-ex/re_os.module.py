#########################################################################
#-*- coding:utf-8 -*-
# File Name: re_os.module.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 02时32分23秒
#########################################################################
#!/usr/bin/env python2.7

import re
import string
f = open('module.txt','r')
lines = f.read()
f.close()
r = re.split(',',lines)
print type(r)
for each in r:
	mm = re.search('\'.+.:',each+'\n')
	if mm is not None:
		print mm.group()

