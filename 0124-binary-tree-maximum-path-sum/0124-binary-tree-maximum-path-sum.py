class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            current_path_sum = node.val + left_max + right_max
            max_sum = max(max_sum, current_path_sum)
            
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_sum