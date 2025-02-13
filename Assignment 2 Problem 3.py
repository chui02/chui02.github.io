def maximumGap(nums):
    maxGap = 0
    #If list has less than 2 numbers
    if len(nums) < 2:
        return 0
    nums.sort()  #Sorts array for ordering
    #Finds max diff between numbers
    for i in range(1, len(nums)):
        maxGap = max(maxGap, nums[i] - nums[i - 1])
    return maxGap

#User input
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Output:", maximumGap(nums))