#########################################################################
#-*- coding:utf-8 -*-
# File Name: _study_re.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月20日 星期日 21时25分16秒
#########################################################################
#!/usr/bin/env python2.7

import re
#using help(re) to know re.
#match() trys to match a string from the start.
#search() trys to looking for a match to the patten.

#ex. looking for email
patt = '\w+@(\w+\.)?\w+\.com'
p = re.match(patt,'nobody@xxx.com').group()
print p
p = re.match(patt,'nobody@www.xxx.com').group()
print p


patt = '\w+@(\w+\.)*\w+\.com'
p = re.match(patt,'nobodu@www.xxx.yyy.zzz.com').group()
print p

p = re.match('\w\w\w-\d\d\d','abc-123')
if p is not None: 
	print p.group()

p = re.match('\w\w\w-\d\d\d','abc-xyz')
if p is not None:
	print p.group()#no output.

p = re.match('(\w\w\w)-(\d\d\d)','abc-123')
if p is not None:
	print p.group()
	print p.group(1)
	print p.group(2)
	print p.groups()
p = re.match('(a(b))','ab')
if p is not None:
	print p.group()
	print p.group(1)
	print p.group(2)
	print p.groups()


#serch 
	#start of a string.
	#erge of a word.
print '----------------'
m = re.search('^The','The end.')
if m is not None:
	print m.group()
m = re.search('^The','end The')#no output.
if m is not None:
	print m.group()

print '***************************'
m = re.search(r'\bthe','bite the dog.')
if m is not None:
	print m.group()
m = re.search(r'\bthe','bitethe dog.')#search for only at start or end.
if m is not None:
	print m.group(),'*****no output.'#no output.

m = re.search(r'\Bthe','bitethe dog.')#not at start or end of a word.
if m is not None:
	print m.group()

