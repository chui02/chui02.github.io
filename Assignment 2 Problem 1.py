def majorityElement(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

#User input
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Output:", majorityElement(nums))