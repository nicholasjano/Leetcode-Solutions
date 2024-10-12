# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorderTraversal(root, [])
    
    def _inorderTraversal(self, node, traversal):
        if not node:
            return traversal
        
        self._inorderTraversal(node.left, traversal)
        traversal.append(node.val)
        self._inorderTraversal(node.right, traversal)

        return traversal