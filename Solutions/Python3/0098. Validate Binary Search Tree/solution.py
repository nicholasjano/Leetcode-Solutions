# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower_bound = float('-inf')
        upper_bound = float('inf')
        queue = deque([(root, lower_bound, upper_bound)])
        while queue:
            node, low, high = queue.popleft()

            if low >= node.val or high <= node.val:
                return False

            if node.left:
                queue.append((node.left, low, node.val))
            
            if node.right:
                queue.append((node.right, node.val, high))
        return True