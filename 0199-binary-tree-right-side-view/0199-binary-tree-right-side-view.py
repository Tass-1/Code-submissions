# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ha = deque([root])
        finale = []
        if not root:
            return []
        def fun(roo,arr):
            while arr:
                for i in range(len(arr)):
                    a = arr.popleft()
                    if a.left:
                        arr.append(a.left)
                    if a.right:
                        arr.append(a.right)
                finale.append(a.val)
        fun(root,ha)
        return finale
