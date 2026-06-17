def ransom(s, t):
    freq={}
    
    for i in t:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] +=1
            
    for i in s:
        if i not in freq or freq[i] ==0:
            return False
        freq[i] -=1
    
    return True
    