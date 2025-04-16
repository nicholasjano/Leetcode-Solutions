# Solution Walk Through
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Intuition
With the preorder traversal, the root node will always be at index 0. With the inorder traversal, any node to the left of the root is within the left subtree, and any node to the right of the root is within the right subtree. This can be broken up recursively for each subtree.

## Approach
- The entire function will be recursive. First, cover the base case if `preorder` or `inorder` are empty, and return None as the node.
- The current root value will be the first index of the `preorder` list. Create a new node for the root. The left/right subtree split point will be taken from the position of the root in the `inorder` list.
- The left and right subtrees can be created recursively, with the `preorder` and `inorder` lists partitioned to only contain the values of each specific subtree.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$