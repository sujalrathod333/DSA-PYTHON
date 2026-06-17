
def findTheDifference(s, t):
        freq={}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1
        
        for i in t:
            if i not in freq or freq[i] ==0:
                return i
            freq[i] -=1
        return False
    
print(findTheDifference("aa", "aat"))