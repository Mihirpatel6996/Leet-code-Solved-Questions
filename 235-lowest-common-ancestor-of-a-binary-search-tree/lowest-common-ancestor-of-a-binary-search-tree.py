# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def func(root, p ,q):
            nonlocal ans
            if root is None:
                return
            if root == p or root == q:
                ans = root
                return
            
            if root.val < p.val:
                func(root.right, p,q)
            elif root.val > q.val :
                func(root.left,p,q)
            else:
                ans = root
                return 
            
        if (p.val < q.val):
            func(root, p ,q)
        else :
            func(root,q,p)
        
        return ans
        