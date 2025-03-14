import heapq
def primeFraction(arr, k):
    n = len(arr)
    minHeap = []
    for i in range(n - 1):
        heapq.heappush(minHeap, (arr[i] / arr[-1], i, n - 1))   #Largeest denominator
    for _ in range(k - 1):
        _, i, j = heapq.heappop(minHeap)
        if j - 1 > i:   #Next smallest denominator
            heapq.heappush(minHeap, (arr[i] / arr[j - 1], i, j - 1))
    _, i, j = heapq.heappop(minHeap) #Getting the k-th smallest fraction
    return [arr[i], arr[j]]

print("Output:", primeFraction([1, 2, 3, 5], 3))
print("Output:", primeFraction([1, 7], 1))