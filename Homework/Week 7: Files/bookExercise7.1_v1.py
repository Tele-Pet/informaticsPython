# 7.11 Exercises Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will look
# asfollows:
# python shout.py
# Enter a file name: mbox-short.txt


usrFile = raw_input('Enter a file name: ')
openFile = open(usrFile)
for line in openFile:
	print line.upper()