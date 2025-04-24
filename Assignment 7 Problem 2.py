import heapq
from collections import defaultdict

def delayTime(time, n, k):
    graph = defaultdict(list)
    for u, v, w in time:    #{source: [(target, weight), ...]}
        graph[u].append((v, w))
    #Min-heap of (distance, node)
    minHeap = [(0, k)]
    dist = {} #Table for distances (shortest time)
    while minHeap:
        time, node = heapq.heappop(minHeap)
        if node in dist:
            #Alr visited
            continue 
        dist[node] = time
        for x, w in graph[node]:
            if x not in dist:
                heapq.heappush(minHeap, (time + w, x))
    if len(dist) == n:
        return max(dist.values())
    else:
        return -1

print(delayTime([[1, 2, 1]], 2, 1))                          #Outputs 1
print(delayTime([[1, 2, 1]], 2, 2))                          #Outputs -1
print(delayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))    #Outputs 2
