#########################################################################
#-*- coding:utf-8 -*-
# File Name: urlopenAuth.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月23日 星期三 21时18分33秒
#########################################################################
#!/usr/bin/env python2.7

import urllib2
LOGIN = 'wesc'
PASSWD = "you'NeverGuess"
URL = 'http://localhost'

def handler_version(url):
	from urlparse import urlparse as up
	hdl = urllib2.HTTPBasicAuthHandler()
	hdl.add_password('Archives',up(url)[1],LOGIN,PASSWD)
	opener = urllib2.build_opener(hdl)
	urllib2.install_opener(opener)
	return url
def request_version(url):
	from base64 import encodestring
	req = urllib2.Request(url)
	b64str = encodestring('%s:%s'%(LOGIN,PASSWD))[:-1]
	req.add_header('Authorization',"Basic %s"%b64str)
	return req

for funcType in ('handler','request'):
	print '***Using %s:'%funcType.upper()
	url = eval('%s_version'%funcType)(URL)
	f = urllib2.urlopen(url)
	print f.readline()
	f.close()
