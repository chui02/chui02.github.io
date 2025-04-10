def path(graph):
    def dfs(node, path):
        if node == len(graph) - 1:
            result.append(path[:])
            return
        for next in graph[node]:
            path.append(next)
            dfs(next, path)
            path.pop()
    result = []
    dfs(0, [0])  #Starting node 0 with path 0
    return result

test1 = [[1,2],[3],[3],[]]
test2 = [[4,3,1],[3,2,4],[3],[4],[]]

print("Example 1 Output:", path(test1))
print("Example 2 Output:", path(test2))