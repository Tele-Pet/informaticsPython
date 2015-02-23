#!/usr/bin/env python
# -*- coding: utf-8 -*-


###############################################################################

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
# 	count = count + 1
# print 'Line count: ', count

###############################################################################

# fhand = open('mbox.txt')
# inp = fhand.read()
# print len(inp)
# print inp[:20]

###############################################################################

# If the file is too large to fit in main memory, you should write your program
# to read the file in chunks using a for or while loop.

###############################################################################

# str.startswith(prefix[, start[, end]]) Return True if string starts with the
# prefix, otherwise return False. prefix can also be a tuple of prefixes to look
# for. With optional start, test string beginning at that position. With
# optional end, stop comparing string at that position.

###############################################################################

# fhand = open('mbox.txt')
# for line in fhand:
# 	if line.startswith('From:'):
# 		print line

###############################################################################

# str.rstrip([chars]) Return a copy of the string with trailing characters
# removed. The chars argument is a string specifying the set of characters to be
# removed. If omitted or None, the chars argument defaults to removing
# whitespace. The chars argument is not a suffix; rather, all combinations of
# its values are stripped:

# >>> '   spacious   '.rstrip()
# '   spacious'
# >>> 'mississippi'.rstrip('ipz')
# 'mississ'

###############################################################################

# fhand = open('mbox.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	# Skip uninteresting license
# 	if not line.startswith('From:'):
# 		continue
# 	# Process our interesting line
# 	print line

###############################################################################

# fhand = open('mbox.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	if line.find('@uct.ac.za') == -1:
# 		continue
# 	print line

###############################################################################

# fname = raw_input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
# 	if line.startswith('Subject:'):
# 		count = count + 1
# print 'There were ', count, 'subject lines in ', fname

###############################################################################

# fname = raw_input('Enter the file name: ')
# try:
# 	fhand = open(fname)
# except:
# 	print 'File cannot be opened: ', fname
# 	exit()
# count = 0
# for line in fhand:
# 	if line.startswith('Subject:'):
# 		count = count + 1
# print 'There were ', count, 'subject lines in ', fname

###############################################################################

# >>> fout = open('output.txt', 'w')
# >>> print fout
# <open file 'output.txt', mode 'w' at 0xb7eb2410>

# If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn’t exist, a new one is created.
# The write method of the file handle object puts data into the file. 

# >>> line1 = 'This here's the wattle,\n'
# >>> fout.write(line1)

###############################################################################

fout = open('output.txt', 'w')
line1 = 'This here\'s the wattle,\n'
line2 = 'Here\'s my line 2, y\'all!\n'
line3 = '...and my line 3\n'
fout.write(line1)
fout.write(line2)
fout.write(line3)
fout.close()
