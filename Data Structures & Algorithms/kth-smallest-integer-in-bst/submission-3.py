# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0

        # Keep going while we have nodes to explore OR ancestors to return to
        while stack or curr:
            # Step 1: Go as far LEFT as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Step 2: We've hit None. The top of the stack is the next smallest
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            
            # Step 3: Visit the right subtree
            curr = curr.right