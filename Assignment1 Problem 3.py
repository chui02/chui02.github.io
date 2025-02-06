def medianOfArrays(array1, array2):
    #Merges both arrays
    arrayMerge = array1 + array2
    
    #Sorts the elements in arrayMerge to clean it up
    arrayMerge.sort()
    
    #Gets the total length of the arrayMerge array.
    n = len(arrayMerge)

    #Calculates median by dividing by 2
    #If its an odd amount of elements it returns the middle element
    if n % 2 == 1:
        median = arrayMerge[n // 2]
    #If its an even amount of elements it returns the average of the two middle elements
    else:
        median = (arrayMerge[n // 2 - 1] + arrayMerge[n // 2]) / 2
    return median

#Example test cases
print(medianOfArrays([1, 3], [2]))  #Outputs 2
print(medianOfArrays([1, 2], [3, 4]))  #Outputs 2.5 (No 0's repeating like in example)