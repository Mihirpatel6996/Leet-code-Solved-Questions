# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None :
                return False
            if p.val != q.val:
                return False
            right = isMirror(p.right,q.left)
            left = isMirror(p.left,q.right)
            if right == True and left == True :
                return True 
            else :
                return False
        
        result = isMirror(root.left, root.right)
        return result

        