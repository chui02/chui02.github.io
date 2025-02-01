def firstAndLast(numbers, target):

    if target not in numbers:
        return [-1, -1]

    #Searches from the start, forwards
    first_position = numbers.index(target)

    #Searches from the end, backwards
    last_position = len(numbers) - 1 - numbers[::-1].index(target)

    return [first_position, last_position]

#Test cases, target number is outside brackets
print(firstAndLast([5,7,7,8,8,10], 8))
print(firstAndLast([5,7,7,8,8,10], 6))
print(firstAndLast([], 0))