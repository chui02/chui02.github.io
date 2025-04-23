from collections import defaultdict

def main(numCourses, prereq):
    graph = defaultdict(list)
    
    for course, prereq in prereq:
        graph[prereq].append(course)
    #0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * numCourses  

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == 2:
            return True     #If alr checked
        visited[course] = 1 #Tracks as having been visited
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 2 #Marks as visited
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True

print(main(2, [[1, 0]]))           #Outputs True

print(main(2, [[1, 0], [0, 1]]))   #Outputs False
