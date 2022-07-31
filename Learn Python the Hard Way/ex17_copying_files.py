import sys
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s..." % (from_file, to_file))

# These two can be done in one line. How?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()
# Gives the length of the string.
print("The input file is %d bytes long." % len(indata))

print("Does the output file exist? %r" % exists(to_file))
input("Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w')  # Can create new file
out_file.write(indata)
out_file.close()
# in_file.close() # Don't need to run as Python closes the file in the same line.

# ______________________________________________________
# SHORT VERSION OF THIS SCRIPT - completed in one line
# open(sys.argv[2], 'w').write(open(sys.argv[1]).read())
