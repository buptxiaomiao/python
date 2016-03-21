#########################################################################
#-*- coding:utf-8 -*-
# File Name: grabWeb.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 21时06分31秒
#########################################################################
#!/usr/bin/env python2.7

from urllib import urlretrieve

def firstNoneBlank(lines):
	for eachline in lines:
		if not eachline.strip():#Dont excute
			continue
		else:#first line excute
			return eachline#return the first line.
def firstlast(webpage):
	f = open(webpage)#file returned by urlretrieve()
	lines = f.readlines()
	f.close()
	print firstNoneBlank(lines)#using func deal with text.
	lines.reverse()
	print firstNoneBlank(lines),

def download(url = 'http://www.baidu.com'):
	try:
	#urlretrieve(url,filename=None,reporthook=None)
		retval = urlretrieve(url)[0]#--return a tuple [0] is file name
		a = urlretrieve(url)
		#print type(a),len(a)
		#for each in a:
		#	print each
		#	print '***************************'
	except IOError:
		retval = None
	if retval :#do some processing
		firstlast(retval)#transfer a file to func
if __name__ == '__main__':
	download()
#retval is return_value
