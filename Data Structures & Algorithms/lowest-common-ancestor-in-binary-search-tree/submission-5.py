# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #idea:
        #run BFS for both points, construct full path
        #two pointer on the nodes and check when the path diverge
        def bfs(root: TreeNode, target:TreeNode) -> List[TreeNode]:
            result = []
            parent_dict: [TreeNode,TreeNode] = {root: None}
            queue = deque([root])
            start = None
            while queue:
                node = queue.popleft()
                if node.val == target.val:
                    start = node
                    break
                children = [node.left, node.right]
                for child in children:
                    if child is not None:
                        parent_dict[child] = node
                        queue.append(child)

            path = []
            cur = start
            while cur is not None:
                path.append(cur)
                cur = parent_dict.get(cur)
            
            return path
        
        pathp = bfs(root, p)[::-1]   # root → ... → p
        pathq = bfs(root, q)[::-1]   # root → ... → q

        l = min(len(pathp), len(pathq))
        ans = root
        for i in range(l):
            if pathp[i].val == pathq[i].val:
                ans = pathp[i]
            else:
                ans = pathp[i-1]
                break
        return ans
        

                



                




