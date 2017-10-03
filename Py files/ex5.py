# Pay attention to %s, %d, %f for representation of string, integer digit, float
# Python format characters doc: https://docs.python.org/2.4/lib/typesseq-strings.html

name = 'Zuck A. Sean'
age = 30 # not a lie
height = 72 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Dark Brown'

pound_to_kilo = 0.453592
inch_to_centimeter = 2.54

height_in_cm = height * inch_to_centimeter
weight_in_kilo = weight * pound_to_kilo

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %f cm tall." % height_in_cm
print "He's %d pounds heavy." % weight
print "He's %f kilos heavy." % weight_in_kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
