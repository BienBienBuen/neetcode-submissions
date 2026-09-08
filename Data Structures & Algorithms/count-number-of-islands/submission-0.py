from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid)
        y = len(grid[0])
        visited = set()
        island_count = 0  # Changed from max_size

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(coord: tuple) -> None:  # Changed from -> int, removed s
            queue = deque()
            queue.append(coord)
            visited.add(coord)
            while queue:
                exploring = queue.popleft()
                p, q = exploring  # Moved this inside the while loop
                for dx, dy in direction:  # Unpack directly
                    child = (p+dx, q+dy)
                    if 0 <= child[0] < x and 0 <= child[1] < y:
                        if grid[child[0]][child[1]] == "1" and child not in visited:  # Added visited check
                            queue.append(child)
                            visited.add(child)

        for i in range(x):
            for j in range(y):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                bfs((i, j))
                island_count += 1  # Changed from area/max_size logic
        
        return island_count  # Changed from max_size