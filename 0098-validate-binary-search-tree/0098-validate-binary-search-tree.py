# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
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
        for i in range(len(s)-1):
            if s[i]>=s[i+1]:
                return False
        return True
            