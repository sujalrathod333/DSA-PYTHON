def countDigits(num):
    count=0
    for i in str(num):
        if num % int(i)==0:
            count+=1
    return count

print(countDigits(8))
    