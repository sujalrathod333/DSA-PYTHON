# find the total of elements 
import numpy as np

array=np.array([2,3,100,4,5,6,7,8,9,1])

total=0
for i in range(len(array)):
    total = total + array[i]
print(total)

