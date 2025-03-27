from typing import List
from collections import deque

class Solution:
    def shortPath(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1: #If only one node exists, doesn't move
            return 0
        fState = (1 << n) - 1 #State when all nodes hhave been visited
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}
        while queue:
            node, mask, dist = queue.popleft()
            if mask == fState:
                return dist
            for next in graph[node]:
                nextNode = mask | (1 << next)
                if (next, nextNode) not in visited:
                    visited.add((next, nextNode))
                    queue.append((next, nextNode, dist + 1))
        return -1

sol = Solution()
graph1 = [[1,2,3],[0],[0],[0]]
print("Output:", sol.shortPath(graph1))

graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print("Output:", sol.shortPath(graph2))