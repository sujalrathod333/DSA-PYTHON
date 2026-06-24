#34 find first and last postion of element in sorted array

def lowerBound(nums, target):
    n=len(nums)
    l=0
    r=n-1
    ans=n
    
    while l<=r:
        mid=(l+r)//2
        if nums[mid] >= target:
            ans = mid
            r=mid-1
        else:
            l=mid+1
    return ans


def upperBound(nums, target):
    n=len(nums)
    l=0
    r=n-1
    ans=n
    
    while l<=r:
        mid=(l+r)//2
        if nums[mid] >target:
            ans = mid
            r=mid-1
        else:
            l=mid+1
    return ans


def searcPosition(nums, target):
    lb= lowerBound(nums, target)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]
    ub= upperBound(nums, target)
    
    return [lb, ub-1]
        


nums = [5,7,7,8,8,10]
target = 8
print(searcPosition(nums, target))