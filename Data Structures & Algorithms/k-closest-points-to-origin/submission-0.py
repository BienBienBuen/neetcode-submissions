import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #turn the list of points into distances wrt origin
        #[(dis, (x, y))]

        heap = []
        for p in points:
            x, y = p
            dist = math.sqrt(x**2 + y**2)
            heap.append((dist, p))

        heapq.heapify(heap)
        result = []

        for i in range(k):
            popped = heapq.heappop(heap)
            result.append(popped[1])

        return result
        

        