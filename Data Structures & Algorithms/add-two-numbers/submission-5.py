# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newnode = ListNode()
        currnode = newnode

        while l1 or l2:
            s = 0
            if not l1:
                s = l2.val + currnode.val
            elif not l2:
                s = l1.val + currnode.val
            else:
                s = l1.val + l2.val + currnode.val


            newval = s % 10
            carry = (s - newval) // 10
            currnode.val = newval
            if carry != 0 or (l1 and l1.next) or (l2 and l2.next):
                currnode.next = ListNode(val=carry)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            currnode = currnode.next
        
        return newnode
        