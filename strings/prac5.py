def validAnagram(s,t):
    if len(s)!=len(t):
        return False
    
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
            
    for i in t:
        if i not in freq and freq[i] ==0:
            return False
        freq[i]-=1
            
    for i in freq.values():
        if i!=0:
            return False
    return True

print(validAnagram("sujal", "lajus"))