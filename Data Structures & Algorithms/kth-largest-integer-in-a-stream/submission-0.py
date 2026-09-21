import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.limit = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.limit:
            heapq.heappop(self.heap)
        return self.heap[0]   # peek, don't pop

        #idea is, we always k elements min heap
        #by popping until only k elements are left, those are the top k
        #then the heap[0] will be the kth

        