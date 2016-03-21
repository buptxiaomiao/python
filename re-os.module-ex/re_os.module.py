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
r = re.split(',',lines)#re.split(pattern,str)--split by pattern
					   #---return a list 
f = open('module_list.txt','w')
for each in r:
	mm = re.search('\'(\w+).:',each+'\n')
	if mm is not None:
		f.write(mm.group(1)+'\n')
f.close()
#re.match(pattern,string)--apply the pattern at start of string
#re.search(pattern,string)--throuth string looking for a match to the patten
			#--return (a) match object(addrs) or None if no match was found.
#re.search().group()--return the string
#re.search('(\w+)(:)').group(1)--return the ((\w+))
#re.search().groups() ---return a list of ((\w+),(:))

