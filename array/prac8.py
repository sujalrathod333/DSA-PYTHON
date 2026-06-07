# two sum

def twoSum(nums, target):
    seen={}
    for i, num in enumerate(nums):
        complete=target-num
        if complete in seen:
            return [seen[complete], i]
        seen[num] = i
        
        
def duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def findDuplicate(nums):
        seen=set()
        for num in nums:
         if num in seen:
             return num
        return False
    
    
    
nums=[1,44,66,77,9,1]
print(duplicate(nums))

