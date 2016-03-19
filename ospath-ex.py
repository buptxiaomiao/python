#########################################################################
#-*- coding:utf-8 -*-
# File Name: ospath-ex.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月19日 星期六 21时00分03秒
#########################################################################
#!/usr/bin/env python2.7

import os
for tmpdir in ('/tmp',r'c:\temp'):
	if os.path.isdir(tmpdir):
		break
else:
	print 'no temp directory available.'
	tmpdir = ''
#os.chdir()
#os.getcwd()--return a string representing the current working directory.
#os.mkdir()
#os.rename(old,new) --rename a file or dir.
#os.listdir(path)	--list_of_strings.
#os.remove(path) 
#os.rmdir(path)
#os.pardir----------parent dir.
#os.path.split(path) --(head,tail)
#os.path.split()
#os.path.splittext(filename)--return (file.txt)
#os.path.basename(path)    ---return final component of a pathname
if tmpdir:
	os.chdir(tmpdir)
	cwd = os.getcwd()
	print '*** current temporary directory'
	print cwd
	
	print '*** creating example directory...'
	os.mkdir('example')
	os.chdir('example')
	
	cwd = os.getcwd()
	print '*** new working directory:'
	print cwd
	print '*** original directory listing:'
	print os.listdir(cwd)
	print '*** creating test file.'
	fjob = open('test','w')	
	fjob.write('foo\n')
	fjob.write('bar\n')
	fjob.close()
	print '*** update directory listing:'
	print os.listdir(cwd)
	
	print '''*** remaining 'test' to 'filetest.txt' '''
	os.rename('test','filetest.txt')
	print '*** updated directory listing:'
	print os.listdir(cwd)

	path = os.path.join(cwd,os.listdir(cwd)[0])
	print '*** full file path name'
	print path
	print '*** (pathname,basename) =='
	print os.path.split(path)
	print '*** (filename,extention) =='
	print os.path.splitext(os.path.basename(path))

	print '*** display file contents:'
	fjob = open(path)
	for each in fjob:
		print each,	
	fjob.close()

	print '*** deleting test file'
	os.remove(path)
	print '*** update directory listing:'
	print os.listdir(cwd)
	os.chdir(os.pardir)###################parent dir.
	print '*** deleting test directory'
	os.rmdir('example')
	print '*** done'
