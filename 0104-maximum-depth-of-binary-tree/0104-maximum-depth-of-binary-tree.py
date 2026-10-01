# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def md(rooty):
            if rooty == None:
                return 0
            left = md(rooty.left)
            right = md(rooty.right)
            if left >= right:
                return left + 1
            else:
                return right + 1
        return md(root)