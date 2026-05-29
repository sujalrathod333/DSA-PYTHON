#find max even number 

arr = [1,2,33,44,55,66,100]

maxEven = -1

for i in range(len(arr)):

    if arr[i] % 2 == 0:

        if arr[i] > maxEven:
            maxEven = arr[i]

print(maxEven)