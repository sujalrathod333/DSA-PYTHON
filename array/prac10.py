mylist=[2,3,4,5,6,1]


def prefixSum(arr):
    n=len(arr)
    ans=[]
    ans.append(arr[0])
    for i in range(1,n):
       ans.append(ans[i-1]+arr[i])
    return ans

print(prefixSum(mylist))