from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Maximum sum from left and right children (only positive parts)
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Path that goes through current node (turning at this node)
            through_node = node.val + left_gain + right_gain
            
            # Update global maximum
            self.global_max = max(self.global_max, through_node)
            
            # Return the maximum gain if we continue the path upward
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.global_max
        