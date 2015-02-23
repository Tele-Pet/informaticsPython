# Write a program to prompt for a file name, and then read through the file and
# look for lines of the form: X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the
# line to extract the floating point number on the line. Count these lines and the
# compute the total of the spam confidence values from these lines. When you reach
# the end of the file, print out the average spam confidence.

# Enter the file name: mbox.txt Average spam confidence: 0.894128046745 Enter the
# file name: mbox-short.txt Average spam confidence: 0.750718518519

import os
# change working direcotry to where .txt files are
os.chdir('/Users/josiah_MBP/Dropbox/Documents/School/Coursera/PythonGIT/Homework/Week 7: Files')

count = 0
spamList = []

usrFile = raw_input('Enter a file path: ')
openFile = open(usrFile)
for line in openFile:
	if line.startswith('X-DSPAM-Confidence: '):
		count = count + 1
		spam = float(line[21:])
		spamList.append(spam)
print 'Average spam confidence: ', (sum(spamList)) / count

