def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract (height, multiply (weight, divide (iq, 2))))

print "that becomes:", what, "Can you do it by hand?"
# Ya. iq divided by 2 is 25, multipled by weight is 4500, subtracted from 
# height is -4426, added to age is -4451