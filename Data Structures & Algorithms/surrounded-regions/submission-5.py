from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # I reckon we do a BFS? on every cell. 
        # terminates in two conditions, when the queue is empty (i.e. all neighbour is X)
        # or during the neighbour stage in BFS, when the neigh is the boundar. 

        #caveat is that one needs to replace in region. 
        #so the data structure on the queue should contain its coordinates
        #when popping from the queue, we need to add the popped items to a list
        #as after terminating, we might need to go through the list to access the coord, and convert
        #the O to the X. 

        r, c = len(board), len(board[0])
        dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        master_visit = set()

    
        def bfs(coord: Tuple) -> None:
            queue = deque([coord])
            visited = set()
            region = []
            can_surround = True

            while queue:
                x, y = queue.popleft()

                if (x, y) in visited:
                    continue
                

                if board[x][y] == "O":
                    if x == r-1 or y == c-1 or x == 0 or y == 0:
                        #we hit the boundary                       
                        #we still let region finish the whole BFS. 
                        can_surround = False

                    region.append((x, y)) #for post processing
                    visited.add((x, y)) #for avoiding duplicates

                    #only consider neighbouring cell of islands
                    for nr, nc in dr:
                        nx, ny = x + nr, y + nc
                        if 0 <= nx <= r-1 and 0 <= ny <= c-1:
                                queue.append((nx, ny)) #for processing its neighbours
            

            for x, y in region:
                master_visit.add((x, y))
                if can_surround == True:
                    board[x][y] = "X"


        for i in range(r):
            for j in range(c):
                if (i, j) not in master_visit:
                    bfs((i, j))



