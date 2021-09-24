def sort_and_square(nums):
    for num in range(len(nums)):
        nums[num] = nums[num] ** 2
    return sorted(nums)


test_input = [-4, -1, 0, 3, 10]
expected = sort_and_square(test_input)
print(expected)
