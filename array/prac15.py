def twoSumII(nums, target):
 left=0
 right=len(nums)-1
 
 while left<right:
     sum = nums[left]+nums[right]
     if sum==target:
         return [left+1,right+1]
     elif sum>target:
          right-=1
     else:
         left+=1
         
print(twoSumII([1,3,6,9,73,80],79))