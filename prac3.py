list=[1,2,3,4,4,6,6,6,7,8,9]

# remove duplicates

def remove_duplicates(lst):
    umique_list=[]
    for num in lst:
     if num not in umique_list:
        umique_list.append(num)
    return umique_list

print(remove_duplicates(list))