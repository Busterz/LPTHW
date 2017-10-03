# This one is like your scripts with argv
def print_two(*args):
    # *args takes all the arguments to the function and then put them together as a list
    # Breaking args into 2 as args is a group of arguments (in this case 2 of them)
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This one is similar to the one above
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothing."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
