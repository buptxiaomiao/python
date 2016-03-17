#!/usr/bin/env python2.7

'readTextfile.py--read and display text file.'
#get filename
fname = raw_input('Enter filename:')

print

#attempt to open tile for reading
try:
	f = open(fname,'r')
except IOError,e:
	print "***file open error:",e
else:
	#display contents to the screen
	for eachline in f:
		print eachline,
	f.close()
