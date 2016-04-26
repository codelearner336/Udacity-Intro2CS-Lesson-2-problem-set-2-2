def median(a,b,c):
    if a>=b and a>=c:
       median = bigger(b,c)
       return median 
    if b>=a and b>=c:
        median = bigger(a,c)
        return median
    if c>=a and c>=b:
        median = bigger(a,b)
        return median
def bigger (x,y):
    if x > y :
        return x
    else :
        return y 
print median (3,7,30)
