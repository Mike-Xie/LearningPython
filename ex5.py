my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
height_cm = my_height * 2.5
my_weight = 180 # lbs
weight_kg = my_weight/2.2
my_eyes = 'Blue'
my_teeth = "White"
my_hair = 'Brown'
my_BMI = (my_weight/(my_height*my_height)) * 703

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He weighs %d pounds." % my_weight # No native speaker says "X is Y pounds heavy."
print "Actually that's not too heavy." 
print "His BMI is %d" %my_BMI
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

# this line is tricky, try to get it exactly right
# challenge accepted 
print "If I add %d, %d, and %d I get %d" % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

# all the format characters
""" 
link is here http://docs.python.org/2/library/stdtypes.html
d, i are for ints,
o is for octal value,
x is for signed hexadecimal
e, E are for floating point exponential format (lower/uppercase)
f, F are for floating point decimal format
g, G are for floating point format with less than -4
c is for single character, accepts int or character
r turns anything into a repr (), printable representation of object so 
when you do eval() it is ideally the same type it was originally
s turns anything into a str()
	)









"""
