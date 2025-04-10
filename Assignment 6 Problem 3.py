def minCost(N, connect):
    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX == rootY:
            return False
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True

    connect.sort(key = lambda x: x[2]) #Edge cost sorted
    costTotal = 0
    edgeCount = 0

    for city1, city2, cost in connect:
        if union(city1, city2):
            costTotal += cost
            edgeCount += 1
    return costTotal if edgeCount == N - 1 else -1 #If invalid

test_cases = [
    (3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]),
    (4, [[1, 2, 3], [3, 4, 4]])
]

for i, (N, connect) in enumerate(test_cases, 1):
    result = minCost(N, connect)
    print(f"Test Example {i} Output: {result}")