# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, traversal, level=0):
            if not node:
                return traversal
            
            if len(traversal) == level:
                traversal.append(node.val)
            
            dfs(node.right, traversal, level + 1)
            dfs(node.left, traversal, level + 1)

            return traversal
        
        return dfs(root, [])
