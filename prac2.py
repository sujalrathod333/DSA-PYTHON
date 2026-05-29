list=[1,2,3,4,5,6,7,8]

# find the max value

def max_value(lst):
    max_value=lst[0]
    for i in lst:
        if i > max_value:
            max_value=i
    return max_value

print(max_value(list))
