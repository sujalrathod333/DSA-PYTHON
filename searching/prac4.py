# search in rotated sorted array

def search(nums, target):
    n=len(nums)
    l=0
    r=n-1
    
    while l<=r:
        mid=(l+r)//2
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[mid] < target <= nums[r]:
                l=mid+1
            else:
                r=mid-1
    return -1


nums = [7,1,2,3,4,5,6,0]
target = 7
                
print(search(nums, target))