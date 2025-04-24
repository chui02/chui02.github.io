def zeroes(nums):
    pointer1 = 0

    for num in nums:
        if num != 0:
            nums[pointer1] = num
            pointer1 += 1

    for i in range(pointer1, len(nums)):
        nums[i] = 0

nums = [0, 1, 0, 3, 12]
zeroes(nums)
print(nums)