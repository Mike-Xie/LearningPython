print "Mary had a little lamb."
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary went."
print "." * 10 # This prints it ten times, concats 9 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# There has got to be a more efficient way to do this. 
# List comprehension

word = "Cheeseburger"
seperated = list(word) #creates a list of characters

reunited = ""
for char in seperated:
	reunited += char


# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
print reunited
