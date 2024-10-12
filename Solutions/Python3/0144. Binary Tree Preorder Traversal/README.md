# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-preorder-traversal/

## Intuition
I can utilize DFS to traverse the Binary Tree.

## Approach
- Utilize DFS to traverse the tree.
- For each node, append the node value to the result list, then recursively traverse the left subtree, and finally recursively traverse the right subtree.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$