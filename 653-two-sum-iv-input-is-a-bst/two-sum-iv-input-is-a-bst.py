# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def getAscending(root):
            stack = []
            t = root

            while t:
                stack.append(t)
                t = t.left

            while stack:
                node = stack.pop()
                yield node.val

                t = node.right
                while t:
                    stack.append(t)
                    t = t.left

        def getDescending(root):
            stack = []
            t = root

            while t:
                stack.append(t)
                t = t.right

            while stack:
                node = stack.pop()
                yield node.val

                t = node.left
                while t:
                    stack.append(t)
                    t = t.right

        asc = getAscending(root)
        desc = getDescending(root)

        left = next(asc, None)
        right = next(desc, None)

        while left is not None and right is not None:
            # Same node ko do baar use nahi karna
            if left >= right:
                return False

            total = left + right

            if total == k:
                return True
            elif total < k:
                left = next(asc, None)
            else:
                right = next(desc, None)

        return False
        