"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #first is exploration via bfs/dfs
        #easiest is to create an adj. But this is two pass
        #for a one pass, do it recursively?
        if not node:
            return None
        
        visited = {}  # original node -> cloned node

        def dfs(n):
            n_c = Node(n.val)
            if n in visited:
                return visited[n]
        
            visited[n] = n_c
 
            for child in n.neighbors:
                n_c.neighbors.append(dfs(child))

            return n_c
        
        return dfs(node)

                