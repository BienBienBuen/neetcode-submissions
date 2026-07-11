# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs? recursively find height of left and right subtree
        #(node, height) in a stack
        def height(node: TreeNode) -> int:
            if node == None:
                return 0
            if node.left == None and node.right == None:
                return 1
            left, right = node.left, node.right
            h_l, h_r = height(left), height(right)
            if h_l is not None and h_r is not None:
                if abs(h_r - h_l) <= 1:
                    return max(h_r, h_l) + 1
                else:
                    return None
            else:
                return None
        
        h = height(root)
        if h is None:
            return False
        else:
            return True
            
        