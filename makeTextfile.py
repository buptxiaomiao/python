#!/usr/bin/env python2.7

'makeTextFile.py--create text file.'

import os
ls = os.linesep

#get filename
while True:
	fname = raw_input("Enter the filename:")
	if os.path.exists(fname):
		print "Error: '%s' already exists"%fname
	else:
		break

#get gile content (text) lines
all=[]
print "\nEnter lines ('.' by itself to quit.)\n"

#loop until user terminates input
while True:
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

#write lines to file with proper line-ending
f = open(fname,'w')
f.writelines(['%s%s'%(x,ls) for x in all])
f.close()
print "Done!"

