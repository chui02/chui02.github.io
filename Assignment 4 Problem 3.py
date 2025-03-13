import heapq
def kLarge(arr, k):
    if not arr or k <= 0:
        return []
    list = []
    n = len(arr)
    maxHeap = [(-arr[0], 0)]    #Negative bc Python only has minHeap, making it negative swaps it around to pop largest element
                                #If I were to try it normally I'd only get the smallest element
                                #Stores value, index
    while k > 0 and maxHeap:
        mx, index = heapq.heappop(maxHeap)   #Max element returned
        list.append(-mx)                 #Returns to positive
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n:
            heapq.heappush(maxHeap, (-arr[left], left))
        if right < n:
            heapq.heappush(maxHeap, (-arr[right], right))
        k -= 1
    return list

print(kLarge([15, 13, 12, 10, 8, 9], 5))