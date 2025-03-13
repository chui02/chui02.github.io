import bisect
def closestElement(arr, k, x):
    left = bisect.bisect_left(arr, x)  #bisect_left from the bisect import to cut and find insert point/closest element
    right = left
    left -= 1
    while k > 0: #Pointers to find k closest elements
        if left < 0:  # If left pointer is out of bounds, move right
            right += 1
        elif right >= len(arr):  #If right pointer out of bounds, moves left
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x): #If left element is closer or equal but smaller in value, moves to left
            left -= 1
        else:
            right += 1                                  #Else moves right
        k -= 1
    return arr[left + 1:right]  #Returns sublist between left + 1 and right in a sorted order

print(closestElement([1, 2, 3, 4, 5], 4, 3))
print(closestElement([1, 2, 3, 4, 5], 4, -1))