# Exercise 2.4 Assume that we execute the following assignment statements: width = 17 
# height = 12.0 For each of the following expressions, write the value of
# the expression and the type (of the value of the expression). 
# 1. width/2 
# 2. width/2.0 
# 3. height/3 
# 4. 1 + 2 * 5 

# Use the Python interpreter to check your
# answers.

width = 17
height = 12.0	

print # print a line break for sake of it looking purdier

a1 = width / 2
print 'a1 equals {0}, {1}'.format(a1, type(a1))

b1 = width / 2.0
print 'b1 equals {0}, {1}'.format(b1, type(b1))

c1 = height / 3
print 'c1 equals {0}, {1}'.format(c1, type(c1))

d1 = 1 + 2 * 5
print 'd1 equals {0}, {1}'.format(d1, type(d1))
