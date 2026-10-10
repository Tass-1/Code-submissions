# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        s = targetSum
        ans = False
        def fun(roo, s):
            nonlocal ans
            p = ans
            if not roo or p == True:
                return
            s -= roo.val
            if s == 0 and (roo.right == None and roo.left == None):
                ans = True
                p = True
            
            print("THe val rn" )
            print(s)
            print("THe root rn")
            print(root.val)
            fun(roo.right , s)
            fun(roo.left , s)
        fun(root,s)
        return ans