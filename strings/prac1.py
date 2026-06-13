def defanfIPaddress(str):
    ans=""
    for i in str:
        if i=='.':
            ans+='[.]'
        else:
            ans+=i
    return ans


print(defanfIPaddress("1.2.4.2.3.6"))