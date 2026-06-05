        
def duplicate2(nums, k):
      seen={}
      for i, num in enumerate(nums):
        if num in seen:
            if i - seen[num] <=k:
                return True
        seen[num]=i
        
      return False
        
nums=[1,2,3,7,3,4]
print(duplicate2(nums, 10))