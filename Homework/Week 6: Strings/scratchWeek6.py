# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# Strings
# fruit = 'banana'
# index = 0
# while index < len(fruit):
# 	letter = fruit[index]
# 	print letter
# 	index = index + 1

###############################################################################

# fruit = 'banana'
# for char in fruit:
# 	print char[0]

###############################################################################


# >>> s = 'Monty Python' 
# >>> print s[0:5] 
# 	Monty 
# >>> print s[6:13] 
# 	Python 

# The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character, INCLUDING THE FIRST BUT EXCLUDING THE LAST.

###############################################################################

# word = 'banana' 
# count = 0
# for letter in word:
# 	if letter == 'a': 
# 		count = count + 1
# 		print count

###############################################################################

# >>> 'a' in 'banana'
# True
# >>> 'seed' in 'apple'
# False

###############################################################################
# def wordBanana(word):
# 	if word == 'banana':
# 		print 'alright banana!'
# 	else:
# 		print 'not a banana'

# wordBanana('red')
# wordBanana('banana')

###############################################################################

# def measureBanana(word):
# 	if word > 'banana':
# 		print 'that word is greater than banana'
# 	else:
# 		print 'banana is greater than that word'

# measureBanana('Pineapple') # Titlecase always comes before lowercase
# measureBanana('pineapple')


###############################################################################

# def count_ord(word):
# 	letterList = []
# 	index = 0
# 	while index < len(word):
# 		for letter in word:
# 			print letter
# 			print ord(letter)
# 			letterList.append(letter)
# 			index = index + 1

# count_ord('Pineapple')

###############################################################################

# >>> stuff = 'hello world'
# >>> dir(stuff)
# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

###############################################################################

# >>> help(str.lstrip)
# Help on method_descriptor:

# lstrip(...)
#     S.lstrip([chars]) -> string or unicode
    
#     Return a copy of the string S with leading whitespace removed.
#     If chars is given and not None, remove characters in chars instead.
#     If chars is unicode, S will be converted to unicode before stripping

###############################################################################

# >>> line=' Herewego '
# >>> line.strip()
# 'Herewego'

###############################################################################

# >>> line = 'Please have a nice day'
# >>> line.startswith('Please')
# True
# >>> line.startswith('p')
# False

###############################################################################

# >>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# >>> atpos = data.find('@')
# >>> print atpos
# 21
# >>> sppos = data.find(' ',atpos)
# >>> print sppos
# 31
# >>> host = data[atpos+1:sppos]
# >>> print host
# uct.ac.za

###############################################################################

# >>> camels = 42
# >>> '%d' % camels
# '42'

# %d --> format an integer
# %g --> format a floating point number
# %s --> format a string

###############################################################################