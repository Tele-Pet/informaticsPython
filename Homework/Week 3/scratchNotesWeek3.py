'''
# Multi-way 'if':
x = 20
if x < 1:
	print 'Small'
elif x < 10:
	print 'Medium'
else:
	print 'Large'
print 'All Done'
'''


'''
# Which line will never print?
x = 1
if x < 2:
	print 'Below 2'
elif x >= 2:
	print '2 or more'
else:
	print 'Something else' # This line will never print
'''


'''
# Which line will never print?
x = 9
if x < 2:
	print 'Below 2'
elif x < 20:
	print 'Below 20'
elif x < 10:
	print 'Below 10' # This line will never print
else:
	print 'Something else'
'''


'''
astr = 'Hello Bob'
try:
	istr = int(astr)
except:
	istr = -1
print 'First', istr

astr = '123'
try:
	istr = int(astr)
except:
	istr = -1
print 'Second', istr
'''

'''
rawstr = raw_input('Enter a number: ')
try:
	ival = int(rawstr)
except:
	ival = -1

if ival >0:
	print 'Nice work'
else:
	print 'Not a number'
'''

'''
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print istr
'''
