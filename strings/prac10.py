def longestString(s):
    n=len(s)
    
    if n == 0:
        return 0
    
    ans=1
    j=1
    i=0
    
    s1=set({})
    s1.add(s[0])
    
    while j<n:
        while s[j] in s1:
            s1.discard(s[i])
            i+=1
        s1.add(s[j])
        ans=max(ans, (j-i+1))
        j+=1
    return ans


print(longestString("abcabcbb"))