from collections import Counter
import heapq

def topKFrequent(nums, x):
    minHeap = [] #Stores x most frequent elements
    map = Counter(nums)
    for num, freq in map.items():
        heapq.heappush(minHeap, (freq, num))
        if len(minHeap) > x:
            heapq.heappop(minHeap)          #Least frequent element gets removed
    return [num for freq, num in minHeap]   #Taking elemennts from heap

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))