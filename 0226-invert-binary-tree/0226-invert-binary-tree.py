# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        def inv(p):
            if p ==None:
                return None
            left = inv(p.left)
            right = inv(p.right)
            temp = p.right
            p.right = p.left
            p.left = temp
            return p
        inv(root)
        return root