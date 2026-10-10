# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        a = None
        def fun(roo):
            nonlocal a
            if not roo:
                return
            a = roo
            l = roo.left
            r = roo.right
            roo.right = None
            roo.left = None
            roo.right = fun(l)
            print(roo)
            if a != None:
                t= a
                t.right = fun(r)
            return roo
        return fun(root)
        