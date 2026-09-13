class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(1) index lookup for inorder
        #post [root, left, ... , right, ....]
        #in [...., left, ..., root, ...., right, ...]
        inorder_index = {val: i for i, val in enumerate(inorder)}
        
        pre_idx = 0  # shared pointer into preorder (root comes first)
        
        def recurr(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx  
            # Base case: empty subtree
            if in_left > in_right:
                return None
            
            # Root is the next preorder value
            root_val = preorder[pre_idx]
            pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Split inorder into left and right by the root's position
            mid = inorder_index[root_val]
            
            # Build left subtree first (preorder gives left before right)
            root.left = recurr(in_left, mid - 1)
            root.right = recurr(mid + 1, in_right)
            
            return root
        
        return recurr(0, len(inorder) - 1)
        