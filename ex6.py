#every one of these is a strong

x = "There are %d types of people." % 10 # %d is an int
binary = "binary"
do_not = "don't" 
y = "Those who know %s and those who %s." % (binary, do_not) # string inside string 1

print x
print y 

print "I said: %r." % x # string inside string
print "I also said: '%s'." % y # string inside string

hilarious = False
joke_evaluation ="Isn't that joke so funny?! %r" #string inside string

print joke_evaluation %hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e #string concac