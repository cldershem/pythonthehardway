from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "Input file is %d bytes long" % len(indata)

if exists(to_file) == True:
	print "Output file exists and is %d bytes long." % len(indata)
	print "RETURN will overwrite, CTRL-C will abort."
else:
	print "File does not exist." 
	print "RETRUN to create file, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Successfully wrote %d of %d bytes to %r" % (len(to_file), len(from_file), to_file)

out_file.close()
in_file.close()
