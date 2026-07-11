# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #right side view of binary tree
        #dfs, right node first. 
        #keep track of level? first node on that level is right?

        #use the previous dfs level set thing. 
        if not root:
            return []
        queue = deque([(root, 1)])
        level_set = []
        while queue:
            node, level = queue.popleft()
            if len(level_set) < level:
                level_set.append([node.val])
            else:
                latest_level = level_set[-1]
                latest_level.append(node.val)
            if node.right is not None:
                queue.append((node.right, level+1))
            if node.left is not None:
                queue.append((node.left, level+1))
        right_view = [level[0] for level in level_set]
        return right_view


