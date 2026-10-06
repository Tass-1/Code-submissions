# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        def fun(ino, post):
            
            if not ino:
                return None
            root = TreeNode(post[-1])
            a = post.pop()
            
            idx = ino.index(a)
            ino.pop(idx)
            root.right = fun(ino[idx:], post)
            root.left = fun(ino[0:idx], post)
            return root
        return fun(inorder , postorder)


