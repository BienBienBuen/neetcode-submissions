from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # 1. Build the edge list with indices instead of point lists
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):  # Only go one way to avoid duplicates
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        # 2. Sort edges by weight (smallest first)
        edges.sort()

        # 3. Union-Find (DSU) to detect cycles
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # They are already connected, adding this edge would create a cycle
            # Union by rank
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        # 4. Kruskal's main loop
        total_cost = 0
        edges_used = 0

        for dist, i, j in edges:
            if union(i, j):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:  # We have a full spanning tree
                    break

        return total_cost
        