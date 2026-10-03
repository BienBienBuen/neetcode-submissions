from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #keep a frontier, check the frontier's neighbour at
        #every time t?
        #the queue should always have the entire exploration frontier. 
        #when we pop, if no neightbour is eligible at time t,
        #we push it to the back of the queue.
        #so at every queue evaluation, we check two things:
        #while node != end and counter < len(queue)


        row, col = len(grid)-1, len(grid[0])-1
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        #(height, coord)
        queue = deque([(grid[0][0], (0, 0))])
        can_swim = set()

        t = 0
        end = (row, col)
        is_end = False

        while not is_end:

            frontier = deque([])
            while queue:
                cur_height, cur_coord = queue.popleft()
                if cur_coord in can_swim:
                    continue

                if cur_height <= t:
                    if cur_coord == end:
                        is_end = True
                        break

                    else:
                        can_swim.add(cur_coord)
                        for dr, dc in direction:
                            r, c = cur_coord
                            nr, nc = r+dr, c+dc
                            if 0 <= nr <= row and 0 <= nc <= col and (nr, nc) not in can_swim:
                                queue.append((grid[nr][nc], (nr, nc)))
                                
                else:
                    frontier.append((cur_height, cur_coord))

            queue = frontier.copy()
            t += 1

        return t-1

                    



