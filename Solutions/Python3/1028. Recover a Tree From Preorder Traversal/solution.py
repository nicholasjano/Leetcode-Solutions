# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        nodes = deque()
        pos = 0
        while pos < n:
            depth = 0
            while pos < n and traversal[pos] == '-':
                depth += 1
                pos += 1

            val = 0
            while pos < n and traversal[pos].isdigit():
                val = val * 10 + int(traversal[pos])
                pos += 1

            nodes.append((depth, val))

        def recoverTree(depth=0): 
            if not nodes or depth != nodes[0][0]:
                return None

            node = nodes.popleft()
            node = TreeNode(node[1])
            node.left = recoverTree(depth + 1)
            node.right = recoverTree(depth + 1)

            return node

        return recoverTree()