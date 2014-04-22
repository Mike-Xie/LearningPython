from sys import argv #imports argument variable which olds arguments

script, filename = argv # unpacks the arguments into seperate containers

txt = open(filename)

print "Here's your file %r: " %filename
print txt.read()

print "Let's mess around with it! What's the new first line?"

txtChange = open(filename, 'w')
line1 = raw_input()

txtChange.write(line1)

print "Type the filename again:"
file_again = raw_input(">") # stores the input

txt_again = open(file_again)

print txt_again.read()