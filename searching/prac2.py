# 35 search insert position

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


def searcPosition(nums, target):
    return lowerBound(nums, target)




nums = [1,3,5,6]
print(searcPosition(nums, 6))