# Exercise 6.4 There is a string method called count that is similar to the
# function in the previous exercise. Read the documentation of this method at
# docs.python. org/library/string.html and write an invocation that counts the
# number of times the letter a occurs in 'banana'.

# Notes from help()
# >>> help(str.count)
# Help on method_descriptor:

# count(...)
#     S.count(sub[, start[, end]]) -> int
    
#     Return the number of non-overlapping occurrences of substring sub in
#     string S[start:end].  Optional arguments start and end are interpreted
#     as in slice notation.

def countLetter(word, usrString):
	print word.count(usrString)

countLetter('banana', 'a')