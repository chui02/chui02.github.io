from collections import deque, defaultdict

def graphPath(n, edges, source, destination):
    if source == destination:
        return True
    graph = defaultdict(list) #Adjacency list builds graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    tracker = set() #BFS
    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        if node not in tracker:
            tracker.add(node)
            for next in graph[node]:
                if next not in tracker:
                    queue.append(next)
    return False

print(graphPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print(graphPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))