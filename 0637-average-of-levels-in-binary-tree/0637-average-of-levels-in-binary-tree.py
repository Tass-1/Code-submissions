# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        ha = deque([root])
        res = []
        def fun(roo,arr):
            nonlocal res
            while arr:
                l = len(arr)
                s = 0
                for i in range(l):
                    a = arr.popleft()
                    s+= a.val
                    if a.left:
                        arr.append(a.left)
                    if a.right:
                        arr.append(a.right)  
                avg = s/l
                res.append(avg)
        fun(root,ha)
        return res

