def countingSort(nums):
    max_num = max(nums)

    count = [0] * (max_num + 1)

    for num in nums:
        count[num] += 1

    result = []

    for value in range(len(count)):
        while count[value] > 0:
            result.append(value)
            count[value] -= 1

    return result


print(countingSort([4, 2, 2, 8, 3, 3, 1]))