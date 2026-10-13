# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ha = deque([root])
        if not root:
            return []
        res = []
        rev = False
        def fun(roo,arr):
            nonlocal res
            nonlocal rev
            while arr:
                l = len(arr)
                t = [node.val for node in arr]
                if rev == False:
                    res.append(t)
                    rev = True
                else:
                    t = t[::-1]
                    res.append(t)
                    rev = False
                for i in range(l):
                    a = arr.popleft()
                    if a.left:
                        arr.append(a.left)
                    if a.right:
                        arr.append(a.right)
        fun(root,ha)
        return res
        