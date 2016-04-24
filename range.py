# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

#Note I have not chosen to treat the cases of 3 equal inputs or 2 equal inputs as edge cases. It could be argued they should be handled differently.

def bigger (a,b):
    if a > b:
        bigger = a
    else:
        bigger = b
    return bigger

def biggest (a,b,c):
    biggest =    bigger (c, (bigger (a,b)))
    return biggest
                  
def smaller (a,b):
    if a < b:
        smaller = a
    else:
        smaller = b
    return smaller

def smallest (a,b,c):
    smallest =    smaller (c, (smaller (a,b)))
    return smallest

def find_range (a,b,c):
    biggest = bigger (c, (bigger (a,b)))
    smallest = smaller (c, (smaller (a,b)))
    the_range = (biggest - smallest)
    return the_range


print find_range (9,9,9)
#0
print find_range (9,9,4)
#5
print find_range (4,7,18)
#14

                  
