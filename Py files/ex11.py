print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
# raw_input returns str data type

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
