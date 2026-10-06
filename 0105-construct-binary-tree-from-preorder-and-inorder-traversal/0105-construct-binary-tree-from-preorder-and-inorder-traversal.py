# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def fun(pre, ino):
            if not ino:
                return None 
            root = TreeNode(pre[0])
            ele = pre[0]
            pre.pop(0)
           
            id = ino.index(ele)
            ino.pop(id)
            root.left = fun(pre , ino[0:id])
            root.right = fun(pre , ino[id:])
            return root
        return fun(preorder,inorder)
