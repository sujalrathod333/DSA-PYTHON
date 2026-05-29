arr=[2,4,1,3,6]

def insertion_arr(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j >=0 and arr[j] > key:
            arr[j+1]=arr[j]
            j -= 1
            
        arr[j+1]=key

    return arr

print(insertion_arr(arr))