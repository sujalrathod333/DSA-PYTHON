# find the total of even numbers
import numpy as np

array=np.array([2,3,100,4,5,6,7,8,9,10])

count = 0
total = 0

for i in range(len(array)):
    if array[i] % 2 == 0:
     count += 1
     total += array[i]
     
        
print(count)
print(total)