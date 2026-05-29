# bubble sort
arr=[1,2,6,3,4]

def bubblesort(arr):
    n=len(arr)
    counts=0
    for i in range(n-1):
     isSWaped=False
     for j in range(n-i-1):
      if arr[j] > arr[j+1]:
         arr[j+1],arr[j] = arr[j],arr[j+1]
         counts+=1
         isSWaped=True

     if not isSWaped:   
            break           
                      
     
    return arr, counts

print(bubblesort(arr))