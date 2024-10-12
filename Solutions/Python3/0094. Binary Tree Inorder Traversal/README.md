# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-inorder-traversal/

## Intuition
I can utilize DFS to traverse the Binary Tree.

## Approach
- Utilize DFS to traverse the tree.
- For each node, recursively visit the left subtree, then append the node value to the result list, and finally recursively traverse the right subtree.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$