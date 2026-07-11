from typing import List, Optional, Tuple
from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def SplitPath(self, path: List[TreeNode], mid: TreeNode) -> Tuple[List[TreeNode], List[TreeNode]]:
        for i, node in enumerate(path):
            if node == mid:
                return path[:i+1], path[i+1:]
        return [], []

    def calculateVal(self, path: List[TreeNode]) -> int:
        return sum(node.val for node in path)

    def findPath(self, r1: TreeNode, r2: TreeNode, root: TreeNode) -> List[TreeNode]:
        parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        path1 = []
        cur = r1
        while cur:
            path1.append(cur)
            cur = parent.get(cur)
        path2 = []
        cur = r2
        while cur:
            path2.append(cur)
            cur = parent.get(cur)
        return path1 + list(reversed(path2))[1:]

    def maxPath(self, root: Optional[TreeNode]) -> Tuple[List[TreeNode], TreeNode, int]:
        if not root:
            return [], None, float('-inf')
        if not root.left and not root.right:
            return [root], root, root.val

        l_path, l_root, l_best = self.maxPath(root.left) if root.left else ([], None, float('-inf'))
        r_path, r_root, r_best = self.maxPath(root.right) if root.right else ([], None, float('-inf'))

        # Process left subtree
        if l_path:
            l1_path, l2_path = self.SplitPath(l_path, l_root)
            l1_val = self.calculateVal(l1_path)
            l2_val = self.calculateVal(l2_path) if l2_path else float('-inf')
            left_down_val = max(l1_val, l2_val)
            if l2_path and l2_val > l1_val:
                left_branch = l2_path
            else:
                left_branch = l1_path
        else:
            left_down_val = float('-inf')
            left_branch = []

        # Process right subtree
        if r_path:
            r1_path, r2_path = self.SplitPath(r_path, r_root)
            r1_val = self.calculateVal(r1_path)
            r2_val = self.calculateVal(r2_path) if r2_path else float('-inf')
            right_down_val = max(r1_val, r2_val)
            if r2_path and r2_val > r1_val:
                right_branch = r2_path
            else:
                right_branch = r1_path
        else:
            right_down_val = float('-inf')
            right_branch = []

        # Path through current root: only add positive contributions from children
        left_contrib = max(0, left_down_val) if left_branch else 0
        right_contrib = max(0, right_down_val) if right_branch else 0
        through_root_val = left_contrib + root.val + right_contrib

        # Best sum in this subtree
        best_val = max(l_best, r_best, through_root_val)

        # Best downward path to return to parent (root alone or root+branch)
        candidates = [(root.val, [root])]  # base
        if left_branch:
            candidates.append((root.val + left_down_val, [root] + left_branch))
        if right_branch:
            candidates.append((root.val + right_down_val, [root] + right_branch))
        down_path = max(candidates, key=lambda x: x[0])[1]
        turning = down_path[-1]

        return down_path, turning, best_val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, _, val = self.maxPath(root)
        return val
        