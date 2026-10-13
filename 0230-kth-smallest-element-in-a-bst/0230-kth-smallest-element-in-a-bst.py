# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        s = []
        def fun(roo):
            nonlocal s
            if not roo:
                return 
            fun(roo.left)
            s.append(roo.val)
            fun(roo.right)
        fun(root)
        print(s)
        return s[k-1]