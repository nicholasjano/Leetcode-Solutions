# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left

            replacement_node = self.findMin(root.right)  
            root.val = replacement_node.val
            root.right = self.deleteNode(root.right, replacement_node.val)
        
        return root
