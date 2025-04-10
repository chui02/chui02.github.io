def cycleGraph(edges):
    n = len(edges)
    tracker = [False] * n  #Tracks if node is visted
    maxLength = -1

    def dfs(node, seen, dMap):
        nonlocal maxLength
        if node == -1:
            return
        if tracker[node]:
            return
        if node in dMap:
            cycleLength = len(dMap) - dMap[node]
            maxLength = max(maxLength, cycleLength)
            return
        dMap[node] = len(dMap)
        dfs(edges[node], seen, dMap)
        tracker[node] = True
        dMap.pop(node)

    for i in range(n):
        if not tracker[i]:
            dfs(i, set(), {})

    return maxLength

print(cycleGraph([3, 3, 4, 2, 3]))
print(cycleGraph([2, -1, 3, 1]))