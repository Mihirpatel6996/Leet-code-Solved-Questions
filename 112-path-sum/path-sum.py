# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def fun(root, current_sum, targetSum):
            if root is None:
                return False
            
            current_sum = current_sum + root.val

            if (root.left is None and root.right is None):
                if current_sum == targetSum:
                    return True
                else:
                    return False
            
            left_result = fun(root.left,current_sum, targetSum)
            right_result = fun(root.right,current_sum,targetSum)
            if left_result or right_result:
                return True

            return False
        
        result = fun(root,0,targetSum)
        return result
        
        

        