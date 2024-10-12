# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._preorderTraversal(root, [])
    
    def _preorderTraversal(self, node, traversal):
        if not node:
            return traversal
        
        traversal.append(node.val)
        self._preorderTraversal(node.left, traversal)
        self._preorderTraversal(node.right, traversal)

        return traversal
        