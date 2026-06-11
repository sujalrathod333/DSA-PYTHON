

def findPow(x,n):
    if n==0:
        return 1
    a=findPow(x,n//2)
    
    if n%2==0:
        return a*a
    else:
        return a*a*2
    
def myPow(x,n):
    if n>=0:
        return findPow(x,n)
    else:
        return 1/findPow(x,n*(-1))

print(myPow(2,6))