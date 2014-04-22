# takes two files and rewrites the second with the first's data

from sys import argv # imports argument variable to ~pack arguments 
# and then you can unpack them into seperate containers 
from os.path import exists #returns True if a file exists

script, from_file, to_file = argv # we are taking 2 files as arguments

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how? Multiple assignment
in_file, indata = open(from_file), in_file.read() 
# in_file grasps from_file
# indata grasps in_file.read()


print "The input file is %d bytes long" % len(indata) #indata contains in_file.read()

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') # out_file grasps to_file (second arg of script)
out_file.write(indata) # outfile is rewritten with in_file.read()

print "Alright, all done."

out_file.close()
in_file.close()