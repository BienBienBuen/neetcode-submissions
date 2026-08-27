import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_dict = {i+1: [] for i in range(n)}
        for u, v, t in times:
            adj_dict[u].append((v, t))
        
        visited = set()
        heap = [(0, k)]

        distance_dict = {i+1: float('inf') for i in range(n)}
        distance_dict[k] = 0
        
        #idea is some variant of diijistra?
        #first, we populate the adj_dict

        while heap:
            dist, node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
            else:
                continue
            
            for child in adj_dict[node]:
                target, time = child
                dist_old = distance_dict[target]
                dist_new = min(dist+time, dist_old)
                distance_dict[target] = dist_new
                heapq.heappush(heap, (dist_new, target))

        if len(visited) < n:
            return -1
        else:
            return max(distance_dict.values())


