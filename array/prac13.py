#remove element

def removeElm(nums, k):
    slow=0
    fast=0
    for fast in range(len(nums)):
        if k != nums[fast]:
            nums[slow]=nums[fast]
            slow+=1
    return slow

arr=[1,2,3,3,3,5,6,7]

print(removeElm(arr, 3))