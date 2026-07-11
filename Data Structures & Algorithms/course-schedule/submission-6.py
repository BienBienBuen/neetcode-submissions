from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Initialize an adjacency list and in-degree array for ALL courses
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        
        # 2. Build the graph and count dependencies
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
            
        # 3. Find all courses with no prerequisites to start
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 4. Process the graph
        courses_taken = 0
        while queue:
            current = queue.popleft()
            courses_taken += 1
            
            # Reduce the in-degree of all courses that depend on the current one
            for dependent_course in graph[current]:
                in_degree[dependent_course] -= 1
                
                # If it has no more prerequisites, we are free to take it
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
                    
        # 5. If we managed to take all courses, there is no cycle
        return courses_taken == numCourses