def maximumSub(num):
    maxsum=num[0]
    currSum=0
    for i in range(len(num)):
        currSum+=num[i]
        if currSum>maxsum:
            maxsum=currSum
        if currSum<0:
            currSum=0
    return maxsum


print(maximumSub([-2,1,-3,4,-1,2,1,-5,4]))