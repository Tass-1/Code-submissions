# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pr = []
        qr = []
        def search(roo, s,arr):
            if not roo:
                return
            arr.append(roo)
            if roo == s:
                return True
            if search(roo.left,s,arr):
                return True
            if search(roo.right,s,arr):
                return True
            arr.pop()
            return False
        search(root, p , pr)
        search(root, q , qr)
        
        i = min(len(pr), len(qr))-1
        while i >= 0:
            pt = pr[i]
            qt = qr[i]
            if pt == qt:
                return pt
            i -= 1