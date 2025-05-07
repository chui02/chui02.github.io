from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        degree[dest] += 1

    #Starting with nodes (basically the courses) that have no prerequisites
    queue = deque([i for i in range(numCourses) if degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            degree[neighbor] -= 1    #If one prerequisite gets satisfied
            if degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == numCourses else []

print(findOrder(2, [[1, 0]]))                           #Output: [0, 1]
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))   #Output: [0, 1, 2, 3]
print(findOrder(1, []))                                 #Output: [0]