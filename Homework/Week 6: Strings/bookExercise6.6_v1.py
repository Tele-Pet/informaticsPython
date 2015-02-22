#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 6.6 
# Read the documentation of the string methods at docs.python. org/lib/string-methods.html. You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

# >>> help(str.replace)
# Help on method_descriptor:

# replace(...)
#     S.replace(old, new[, count]) -> string
    
#     Return a copy of string S with all occurrences of substring
#     old replaced by new.  If the optional argument count is
#     given, only the first count occurrences are replaced.


>>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> data.replace('@', 'google.com')
'From stephen.marquardgoogle.comuct.ac.za Sat Jan 5 09:14:16 2008'