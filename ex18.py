"""
Functions do 3 things:
1. Can name pieces of code like primitives 
2. Take arguments like argv 
3. Lets us make mini-scripts

Created with the keyword 'def' followed by name(arguments):
Don't forget the colon!
"""

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" %arg1

# this takes no arguments
def print_none():
	print "I got nothin'."

print_two("Mike","Xie")
print_two_again("Mike", "Xie")
print_one("First!")
print_none()