class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def longest_path(node):
            if not node:
                return 0
            
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            self.diameter = max(self.diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return self.diameter
