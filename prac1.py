list=[1,2,3,4,5,6,7,8]

def reverse_list(lst):
    left=0
    right=len(lst)-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1

    return lst

print(reverse_list(list))