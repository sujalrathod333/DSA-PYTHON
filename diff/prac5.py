def smallerNumbersThanCurrent(nums):
    count=[]
    for i in nums:
        c=0
        for j in nums:
            if i>j:
             c+=1
        count.append(c)
    return count

print(smallerNumbersThanCurrent([8,1,2,2,3]))