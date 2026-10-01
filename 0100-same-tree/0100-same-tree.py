# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def isSame(p,q):
            if (p == None and q != None) or ( q == None and p != None):
                return False
            if p == None and q == None:
                return True
            if p.val != q.val:
                return False
            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)
            return left and right
        return isSame(p,q)
