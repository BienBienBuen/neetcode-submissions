# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we maintain a heap
        #heap is of size k. this is essentially ranking the top
        #elements in each sublist. 
        #it should be a tuple keeping track of which sublist it
        #came from. after pop we extract index i+1 from the sublist
        if not lists or not lists[0]:
            return None

        heap = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(heap)
        output = []
        while heap:
            val, i, node = heapq.heappop(heap)
            output.append(node)
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        
        for i, node in enumerate(output[:-1]):
            node.next = output[i+1]
        return output[0]





        


        