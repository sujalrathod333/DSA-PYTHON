def substring(s):
    n=len(s)
    ans=0
    for i in range(1, n-2):
        if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
            ans +=1
    return ans

print(substring("aababcabc"))