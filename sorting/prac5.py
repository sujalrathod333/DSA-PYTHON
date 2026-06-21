def partition(nums, low, high):
    pivot = nums[high]  # last element as pivot

    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1


def quickSort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)

        quickSort(nums, low, pi - 1)
        quickSort(nums, pi + 1, high)


def sortedArray(nums):
    quickSort(nums, 0, len(nums) - 1)
    return nums


print(sortedArray([2, 5, 1, 8, 3, 4]))