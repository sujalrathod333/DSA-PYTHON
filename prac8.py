import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])

largest = arr[0]

for n in range(len(arr)):
    while arr[n] > largest:
        largest = arr[n]
print(largest)