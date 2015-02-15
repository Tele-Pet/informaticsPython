# Exercise 4.7 Rewrite the grade program from the previous chapter using a function called computeGrade that takes a score as its parameter and returns a grade as a string.
# Score Grade >0.9 A >0.8 B >0.7 C >0.6 D <=0.6 F


def computeGrade(x):
	if x >= 0.9:
		print 'A'
	elif x >= 0.8:
		print 'B'
	elif x >= 0.7:
		print 'C'
	elif x >= 0.6:
		print 'D'
	elif x < 0.6:
		print 'F'

def collectGrade():
	score = 0.0
	while True:
		try:
			score = float(raw_input("Enter a score between 0.0 and 1.0: "))
		except: 
			print 'That\'s not a number. Please try again.'
		else:
			if 0.0 <= score <= 1.0:
				computeGrade(score)
				break # Comment this out if you'd like to loop it all
			else:
				print 'That\'s out of range.  Try again.'

collectGrade()

