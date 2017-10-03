from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The inpurt file is %d bytes long" % len(indata)

# exists() returns boolean value
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit ENTER or RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# always remember to close the opened files at the end
out_file.close()
in_file.close()
