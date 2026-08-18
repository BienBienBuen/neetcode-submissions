class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #same as the prereq one, but now need to return the path
        #Apply DFS iteratively? find connected components

        #or topological sort, which doesn't work that well. 

        #BFS also works. While applying BFS, we keep the traversal order
        #basically, after popping out of the queue, we add it elsewhere
        #use the indegree for each node. starting with indegree = 0
        indegree = {i: 0 for i in range(numCourses)}
        graph = defaultdict(list)   

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course) 

        #we iterate over graph_set via some iterator?
        #khan

        #from collections import deque
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []

        while queue:
            visiting = queue.pop()
            result.append(visiting)
            dependencies = graph[visiting]
            for course in dependencies:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        if len(result) == numCourses:
            return result
        else:
            return []


        