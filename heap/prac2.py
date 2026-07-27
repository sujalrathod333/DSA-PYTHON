#1046 last stone weight

import heapq

def lastStone(stones):
    h=[]
    
    for i in stones:
        heapq.heappush(h, -i)
    while len(h)>1:
        a=-heapq.heappop(h)
        b=-heapq.heappop(h)
        
        diff=a-b
        if diff>0:
            heapq.heappush(h, -diff)
            
    if len(h)==0:
        return 0
    else:
        return -h[0]


stones=[2,7,4,1,8,1]
print(lastStone(stones))
        