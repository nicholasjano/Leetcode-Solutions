class Solution:
    def maxHeightTree(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        leftHeight = self.maxHeightTree(node.left)
        rightHeight = self.maxHeightTree(node.right)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1
    
    def createTreeList(self, root: Optional[TreeNode], maxHeight: int) -> List[List[str]]:
        treeStringList = [[""] * (2 ** maxHeight - 1) for _ in range(maxHeight)]
        queue = deque([(root, 0, (2 ** maxHeight - 1) // 2)])

        while queue:
            node, currentHeight, index = queue.popleft()

            treeStringList[currentHeight][index] = str(node.val)

            offset = 2 ** (maxHeight - currentHeight - 2)

            if node.left is not None:
                queue.append((node.left, currentHeight + 1, index - offset))

            if node.right is not None:
                queue.append((node.right, currentHeight + 1, index + offset))
        
        return treeStringList
    
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root is None:
            return []
        
        maxHeight = self.maxHeightTree(root)
        return self.createTreeList(root, maxHeight)