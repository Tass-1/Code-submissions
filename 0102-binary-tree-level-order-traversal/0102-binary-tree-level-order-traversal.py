# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ha = deque([root])
        if not root:
            return []
        res = []
        def fun(roo,arr):
            nonlocal res
            while arr:
                l = len(arr)
                res.append([node.val for node in arr])
                for i in range(l):
                    a = arr.popleft()
                    if a.left:
                        arr.append(a.left)
                    if a.right:
                        arr.append(a.right)
        fun(root,ha)
        return res