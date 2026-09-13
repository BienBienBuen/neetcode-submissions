from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None or subRoot is None:
            return False

        isEqual = True
        queue = deque([root])
        matching_root = False
        m_root = None

        def dfs(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)

        while queue and not matching_root:
            visiting = queue.popleft()

            if visiting.val == subRoot.val:
                if dfs(visiting, subRoot):
                    matching_root = True
                    m_root = visiting

            if visiting.left is not None:
                queue.append(visiting.left)
            if visiting.right is not None:
                queue.append(visiting.right)

        return dfs(m_root, subRoot) if m_root is not None else False
        