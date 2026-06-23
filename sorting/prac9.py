# non overlap intervals

def nonOverlap(intervals):
    intervals.sort(key=lambda x:x[1])
    count=0
    prev=intervals[0][1]
    
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start >= prev:
            prev=end
        else:
            count+=1
    return count
        
    



intervals = [[1,2],[2,3],[3,4],[1,3]]
print(nonOverlap(intervals))