def kidsWithCandies(nums, extraCandies):
    maxCandies = max(nums)
    ans=[]
    for i in nums:
        if (i+extraCandies) >= maxCandies:
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(kidsWithCandies([2,3,5,1,3], 3))