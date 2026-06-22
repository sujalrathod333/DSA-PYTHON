# merge sorted array

def mergeSort(n1,k,n2,l):
    i=k-1
    j=l-1
    m=k+l-1
    
    while i>=0 and j>=0:
        if n1[i]>n2[j]:
            n1[m] = n1[i]
            i-=1
        else:
            n1[m] = n2[j]
            j-=1
        m-=1
        
    while j>=0:
        n1[m] = n2[j]
        j-=1
        m-=1
        
        
    return n1
                
    
a=[1,2,3,0,0,0]
b=[2,4,5]

ans = mergeSort(a, 3, b, 3)
print(ans)