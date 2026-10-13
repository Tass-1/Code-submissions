# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        s = []
        def fun(roo):
            nonlocal res
            nonlocal s
            if not roo:
                return 
            fun(roo.left)
            s.append(roo.val)
            fun(roo.right)
            
            

        fun(root)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                res = min(res , abs(s[i]-s[j]))
        return res
