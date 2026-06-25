#875 koko eating bananas

def findHours(arr, mid):
    ans=0
    for pile in arr:
       ans += (pile + mid -1) // mid
    return ans
    
def minEating(arr, h):
    l=1
    r=max(arr)
    k=r
    
    while l<=r:
        mid=(l+r)//2
        if findHours(arr, mid) <= h:
            k=mid
            r=mid -1
        else:
            l=mid +1
    return k


        
piles = [3,6,7,11]
h = 8
print(minEating(piles, h))