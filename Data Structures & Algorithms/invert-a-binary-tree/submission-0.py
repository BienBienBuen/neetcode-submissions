# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #surely we use recursion?
        if root == None:
            return None
            
        if root.left == None and root.right == None:
            return root

        left = root.left
        right = root.right
        inverted_l = self.invertTree(left)
        inverted_r = self.invertTree(right)
        root.left = right
        root.right = left
        return root
        