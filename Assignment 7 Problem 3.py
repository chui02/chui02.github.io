class NodeConnect:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  #If already connected
        self.parent[px] = py
        return True

def minCost(n, wells, pipes):
    edges = []
    for i in range(n):  #Adds virtual edges from node 0 to each house
        edges.append((wells[i], 0, i + 1))  #(cost, from, to)

    for u, v, w in pipes:
        edges.append((w, u, v))

    edges.sort() #Edges get sroted by cost

    nc = NodeConnect(n + 1)  #0 is virtual node, 1 to n are the houses
    totalCost = 0
    for cost, u, v in edges:
        if nc.union(u, v):
            totalCost += cost
    return totalCost

n = 3
wells = [1, 2, 2]
pipes = [[1, 2, 1], [2, 3, 1]]
print(minCost(n, wells, pipes))  #Outputs 3