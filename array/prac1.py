# find the smallest elements 
import numpy as np

array=np.array([2,3,100,4,5,6,7,8,9,1])

min=array[0]

for i in range(len(array)):
   if array[i] > min:
      min = array[i] /2
print(min)
