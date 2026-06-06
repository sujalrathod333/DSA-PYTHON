nums=[2,4,6,1,2,6,8,9,3]

def sortArray(nums):
    n=len(nums)
    start=0
    for i in range(n):
        if nums[i] % 2 != 0:
            nums[i], nums[start] = nums[start], nums[i]
            start+=1
    return nums

print(sortArray(nums))