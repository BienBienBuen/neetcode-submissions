# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node) -> height:
            if node is None:
                return 0
            else:
                l, r = node.left, node.right
                h_l = max(height(l), height(r))+1
                return h_l
        return height(root)


        