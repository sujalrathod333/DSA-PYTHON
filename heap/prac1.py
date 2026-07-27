#215 find the kth largest element in an array

import heapq

def findkthlargest(nums, k):
    h=[]
    
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]

nums=[2,6,1,9,4,3,]
print(findkthlargest(nums, 3))