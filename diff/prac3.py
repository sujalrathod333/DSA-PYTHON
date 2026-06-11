def fizzBuzz(n):
    ans=[]
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            ans.append("fizzbuzz")
        elif i%3==0:
            ans.append("fizz")
        elif i%5==0:
            ans.append("buzz")
        else:
            ans.append(str(i))
    return ans


print(fizzBuzz(15))