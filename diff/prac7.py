def isPalindrome(x):
    temp=x
    rev=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    return rev==x

print(isPalindrome(121))