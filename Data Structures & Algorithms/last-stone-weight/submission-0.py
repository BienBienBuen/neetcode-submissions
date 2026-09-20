import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #do a heap operation. 
        stone_heap = [-s for s in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            s1 =  -heapq.heappop(stone_heap) 
            s2 =  -heapq.heappop(stone_heap) 
            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(stone_heap, -(s2 - s1))
            else:
                heapq.heappush(stone_heap, -(s1 - s2))
            
        
        if len(stone_heap) == 1:
            return -heapq.heappop(stone_heap) 
        else:
            return 0
