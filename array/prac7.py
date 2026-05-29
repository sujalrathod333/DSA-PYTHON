# find the second largest even number


arr = [1,2,33,44,55,66,100]

maxEven = -1
secondLarge = -1

for i in range(len(arr)):

    if arr[i] % 2 == 0:
        
        if arr[i] > maxEven:
            secondLarge = maxEven
            maxEven = arr[i]
        elif arr[1] > secondLarge:
            secondLarge = maxEven
            

print(secondLarge)