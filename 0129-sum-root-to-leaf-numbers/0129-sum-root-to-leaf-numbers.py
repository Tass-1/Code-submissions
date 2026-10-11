# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = 0
        val = []
        def fun(roo, t):
            nonlocal total
            if not roo:
                return None
           
            t.append(str(roo.val))
            a = fun(roo.left,t)
            b = fun(roo.right,t)
            if a or b:
                t.pop()
                return total
            else:
                s = int("".join(t))
                print(s)
                total += int(s)
                t.pop()
                return total
        s = ""
        fun(root,val)
        return total
            