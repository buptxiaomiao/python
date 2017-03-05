#########################################################################
#-*- coding:utf-8 -*-
# File Name: gendata.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月20日 星期日 22时08分05秒
#########################################################################
#!/usr/bin/env python2.7

from random import randint,choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com','edu','net','org','gov')

for i in range(randint(5,10)):#randint()---return an int range(5,10)
	dtint = randint(0,maxint-1)#sys.maxint---the largest supported integer.
								#sys
	dtstr = ctime(dtint)#time.ctime(seconds)
						#--return a Thu Jan 1 08:00:00 1970+sec
	shorter = randint(4,7)
	em = ''
	for j in range(shorter):#shorter is size of em.
		em += choice(lowercase)
	longer = randint(shorter,12)#longer is size of dn.
	dn = ''
	for j in range(longer):
		dn += choice(lowercase)#random.choice(seq)
							   #--return a random item from the seq
							#lowercase is a string 'abc...z'
	print '%s::%s@%s.%s::%d-%d-%d'%(
		dtstr,em,dn,choice(doms),dtint,shorter,longer)

