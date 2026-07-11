# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #basically dfs here. lets try to finish this. 

        good = 0
        stack = [(root.val, root)]
        #(max_val down this path, the node itself)
        while stack:
            prev_max, node = stack.pop()
            if node:
                if node.val >= prev_max:
                    good += 1
                curr_max = max(prev_max, node.val)
                stack.append((curr_max, node.left))
                stack.append((curr_max, node.right))
        return good

