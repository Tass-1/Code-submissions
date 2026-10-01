# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return None
        res = True
        def inv(p,q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                print(p,q)
                return False
            elif p.val != q.val:
                print(p.val , q.val)
                return False
            left = inv(p.left , q.right)
            right = inv(p.right , q.left)
            return (left and right)
        return inv(root.left,root.right)