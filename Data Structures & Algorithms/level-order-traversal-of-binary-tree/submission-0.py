# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #literally just BFS? 
        if not root:
            return []
            
        levelset = [[]]
        queue = deque([(root, 1)])
        currlevel = 1
        while queue:
            node, lvl = queue.popleft()
            if node is not None:
                if lvl == currlevel:
                    levelset[-1].append(node.val)
                else:
                    levelset.append([node.val])
                    currlevel+=1
                queue.append((node.left, lvl+1))
                queue.append((node.right, lvl+1))
        return levelset
