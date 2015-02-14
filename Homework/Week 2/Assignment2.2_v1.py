# 2.2 Write a program that uses raw_input to prompt a user for their name and 
# then welcomes them. Note that raw_input will pop up a dialog box. Enter 
# Sarah in the pop-up box when you are prompted so your output will match the 
# desired output.

# Desired output: 'Hello Sarah'

# Request user name
name = raw_input('What is your name? ')
# Print personalized greeting to user
print 'Hello ' + name

# Note:
# Could not run the below, even though it works.  System online is sort of prescribed.

# Desired output: 'Hello Sarah'

# Request user name
# name = raw_input('What is your name? ')
# # Print personalized greeting to user
# print 'Hello {}'.format(name)

