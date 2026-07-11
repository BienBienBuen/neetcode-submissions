class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #BFS. How? How to do with a matrix?

        #queue
        queue = deque()
        y = len(grid)
        x = len(grid[0])
        for i, sublist in enumerate(grid):
            for j, item in enumerate(sublist):
                if item == 0:
                    queue.append((i,j))

        chests = set(queue)
        visited: Dict[tuple:int] = {}

        while queue:
            node = queue.popleft()
            p = 0
            if node not in chests:
                p = visited[node]

            i, j = node
            children = [(i, j+1), (i, j-1), (i+1, j), (i-1,j)]

            for child in children:
                a, b = child
                if 0 <= a < y and 0 <= b < x  and grid[a][b] == 2147483647:
                    if (a, b) in visited:
                        visited[(a, b)] = min(visited[(a, b)], p+1) 
                        grid[a][b] = visited[(a, b)]
                    else:
                        visited[(a, b)] = p+1
                        grid[a][b] = p+1
                        queue.append((a, b))
        




        