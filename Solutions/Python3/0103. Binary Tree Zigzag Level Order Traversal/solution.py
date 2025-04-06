# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []

        curr_level_queue = deque([])
        queue = deque([root])

        while queue:
            level = len(traversal)
            nodes_in_level = len(queue)
            for _ in range(nodes_in_level):
                node = queue.popleft()
                
                if level % 2 == 0:
                    curr_level_queue.append(node.val)
                else:
                    curr_level_queue.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            traversal.append(list(curr_level_queue))
            curr_level_queue.clear()
        
        return traversal