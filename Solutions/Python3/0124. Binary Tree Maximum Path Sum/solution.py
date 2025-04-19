# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, float("-inf"))
            
            left_max, result_left = dfs(node.left)
            right_max, result_right = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            split_sum = left_max + right_max + node.val

            result = max(result_left, result_right, split_sum)

            return (node.val + max(left_max, right_max), result)
        
        if not root:
            return 0

        return dfs(root)[1]