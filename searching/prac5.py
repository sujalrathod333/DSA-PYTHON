#852 peak ibdex in mountain array

def peakMount(arr):
    n=len(arr)
    l=0
    r=n-1
    
    while l<r:
        mid=(l+r)//2
        if arr[mid] < arr[mid + 1]:
            l=mid + 1
        else:
            r = mid
    return l


nums = [1,3,5,7,15,6,4,2,0]
print(peakMount(nums))