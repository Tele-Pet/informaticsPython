# Exercise4.3 Movethefunctioncallbacktothebottomandmovethedefinitionof print_lyrics after the definition of repeat_lyrics. What happens when you run this program?

# Definitions/Functinos can be in any order, with output always the same.



def print_lyrics():
	print "I'm a lumberjack, and I'm okay." 
	print 'I sleep all night and I work all day.'

def repeat_lyrics(): 
	print_lyrics() 
	print_lyrics()

repeat_lyrics()

# Note:
# What’s the moral of this sordid tale? When you read a program, you don’t always want to read from top to bottom. Sometimes it makes more sense if you follow the flow of execution.



