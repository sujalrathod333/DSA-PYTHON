def rich(accounts):
    ans =0
    for accounts in accounts:
        ans = max(ans, sum(accounts))
    return ans
    
    
    
accounts = [[1,5],[7,3],[3,5]]
print(rich(accounts))