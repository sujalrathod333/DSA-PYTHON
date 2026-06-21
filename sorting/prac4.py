def mergesort(nums, l, mid, r):
    a = nums[l:mid+1]
    b = nums[mid+1:r+1]

    i = 0
    j = 0
    k = l

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            nums[k] = a[i]
            i += 1
        else:
            nums[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        nums[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        nums[k] = b[j]
        j += 1
        k += 1


def merge(nums, l, r):
    if l >= r:
        return

    mid = (l + r) // 2

    merge(nums, l, mid)
    merge(nums, mid + 1, r)

    mergesort(nums, l, mid, r)


def sortedArray(nums):
    merge(nums, 0, len(nums) - 1)
    return nums


print(sortedArray([2, 5, 1, 8, 3, 4]))