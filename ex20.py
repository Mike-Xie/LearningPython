from sys import argv

#Test File
"""
# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line
"""
#global variables
script, input_file = argv


#helper functions
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def forwardOne(f):
	f.seek(1)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)


#calls
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
"""
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
"""
print "Let's see what forwardOne does:"

rewind(current_file)

forwardOne(current_file)

print current_file

forwardOne(current_file)

print current_file

forwardOne(current_file)

print current_file
