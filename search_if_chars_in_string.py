
# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string.


# email me if you know a one line solution to this. I tried any/all etc but they seem to be string match

def string_search(debris, product):
    ### WRITE YOUR CODE HERE #

    n = len(product)
    x=0
    while x < n:
        if product[x] in debris:
            x= x+1
        else:
            return False
    return True     

### TEST CASES ###
print string_search ('abc','babad')   
print "Test case 1: ", string_search('UdaciousUdacitee', 'Udacity')
print "Test case 2: ",string_search('buy me dat Unicorn', 'Udacity')
print "Test case 3: ", string_search('AEIOU and sometimes y... c', 'Udacity') 
print "Test case 4: ", string_search('wsx0-=mttrhix', 't-shirt') 
