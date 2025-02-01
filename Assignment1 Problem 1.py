def twoSum(numbers, target):
    num_map = {}  #Store numbers and indices
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]  #Returns the indices of given two numbers
        num_map[num] = i  #Stores number and index

#Example test cases, target number is outside brackets
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))