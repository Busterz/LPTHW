#from sys import argv

#script, input_index = argv

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def printAnswers(index):
    """Print the answers to the list 'animals' in ex34"""
    #index = input_index
    if(index == 0):
        index_name = "1st"
    elif(index == 1):
        index_name = "2nd"
    elif(index == 2):
        index_name = "3rd"
    else:
        index_name = str(index + 1) + "th"

    print "The %s animal is at %d and is a %s." % (index_name, index, animals[index])
    print "The animal at %d is the %s animal and is a %s." % (index, index_name, animals[index])

# Type from ex34 import * to avoid repetitive ex34.sth
