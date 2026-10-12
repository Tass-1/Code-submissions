# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def gdpth(roo, il):
            d = 0
            while roo:
                d += 1
                roo = roo.left if il else roo.right
            return d

        def fun(roo):
            if not roo:
                return 0
            left = gdpth(roo, True)
            right = gdpth(roo, False)
            if left == right:
                return (1<<left) -1
            else:
                return 1 + fun(roo.left) + fun(roo.right)
        return fun(root)