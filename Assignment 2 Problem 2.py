def kLargestElement(nums, k):
    nums.sort(reverse=True)  #Sorts descending order
    return nums[k - 1]  #Returns k-th largest element in list

#User input
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
k = int(input("Enter k: "))
print("Output:", kLargestElement(nums, k))