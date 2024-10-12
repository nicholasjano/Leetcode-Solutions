# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._postorderTraversal(root, [])

    def _postorderTraversal(self, node, traversal):
        if not node:
            return traversal
        
        self._postorderTraversal(node.left, traversal)
        self._postorderTraversal(node.right, traversal)
        traversal.append(node.val)

        return traversal