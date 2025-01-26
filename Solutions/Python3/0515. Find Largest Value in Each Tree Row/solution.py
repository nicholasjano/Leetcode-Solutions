# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])
        current_level = -1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                result.append(node.val)
                current_level = level
            else:
                result[current_level] = max(result[current_level], node.val)
            
            if node.left:
                queue.append((node.left, current_level + 1))

            if node.right:
                queue.append((node.right, current_level + 1))
        
        return result