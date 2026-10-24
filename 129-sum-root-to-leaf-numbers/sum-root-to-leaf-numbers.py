# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def fun(root, current_number):
            if root is None:
                return 0
            
            path.append(root.val)
            current_number = current_number * 10 + root.val

            if (root.left is None and root.right is None):
                return current_number
            
            left_sum = fun(root.left,current_number)
            right_sum = fun(root.right,current_number)

    
            return left_sum + right_sum
           

        
        return fun(root,0)

        
        
        