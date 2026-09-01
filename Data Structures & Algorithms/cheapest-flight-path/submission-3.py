import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s, d, price in flights:
            adj[s].append((price, d))

        visited = set()                     # ← NEW
        heap = [(0, 0, src)]                # (cost, steps, node)

        while heap:
            cost, steps, node = heapq.heappop(heap)

            if (node, steps) in visited:    # ← NEW
                continue
            visited.add((node, steps))      # ← NEW

            if node == dst:
                return cost                 # first time we pop dst is the cheapest

            if steps > k:                   # we already have steps > k, can't go further
                continue

            for price, nxt in adj[node]:
                heapq.heappush(heap, (cost + price, steps + 1, nxt))

        return -1