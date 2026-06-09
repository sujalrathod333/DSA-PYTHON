
def powerofTwo(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2!=0:
        return False
    return powerofTwo(n//2)


n=16
print(powerofTwo(n))