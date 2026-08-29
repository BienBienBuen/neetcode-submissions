import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #construct a tree between points. 
        #minimum cost. min distance tree.
        #start at an arbitary point. find closest neighbour?

        #ok first we have to construct an adjacency list?
        n = len(points)
        adj = {(points[i][0], points[i][1]): [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):  # Only go one way to avoid duplicates
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                #add points into adj
                adj[(x1, y1)].append((dist, (x2, y2)))
                adj[(x2, y2)].append((dist, (x1, y1)))
        
        #priority queue bfs
        queue = [(0, (points[0][0], points[0][1]))]
        visited = set()
        cost = 0
        #start at arbitary place
        while len(visited) < n:
            c, point = heapq.heappop(queue)
            if point in visited:
                continue
            visited.add(point)
            cost += c

            #node as structure (dist, (x2, y2))
            neighbours = adj[point]
            for node in neighbours:
                if node[1] not in visited:
                    heapq.heappush(queue, node)

        return cost


            #need some way to check if this poped edge creates a cycle. 
            #need union find?
            