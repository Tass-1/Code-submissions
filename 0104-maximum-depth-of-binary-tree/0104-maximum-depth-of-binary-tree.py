# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        d = 1

        def md(rooty):
            if rooty == None:
                return 0
            left = md(rooty.left)
            right = md(rooty.right)
            return max(left, right)+1
        k = md(root)
        
        return k