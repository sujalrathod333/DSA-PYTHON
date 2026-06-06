nums=[1,1,2,2,4,4,4,7,7,7,7,7,8,9,9,9]

def removeDuplicates(nums):
        n=len(nums)
        start=0

        for i in range(1,n):
            if nums[i]!=nums[start]:
             start+=1
             nums[start]= nums[i]
        return start+1

def removeDuplicatesII(nums):
        n=len(nums)
        start=1

        for i in range(1,n):
            if nums[i]!=nums[start-1]:
             start+=1
             nums[start]= nums[i]
        return nums[:start+1]

print(removeDuplicatesII(nums))