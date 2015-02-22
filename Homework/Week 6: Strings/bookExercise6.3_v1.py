# Exercise 6.3 Encapsulate this code below in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# word = 'banana' 
# count = 0
# for letter in word:
# 	if letter == 'a': 
# 		count = count + 1
# 		print count
def count(yourString, yourLetter):
	count = 0
	for letter in yourString:
		if letter == yourLetter:
			count = count + 1
	print 'The letter \'{0}\' appears {1} times in the word \'{2}\'.'.format(yourLetter, count, yourString)

# example:
count('California', 'a')

