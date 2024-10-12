# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-postorder-traversal/

## Intuition
I can utilize DFS to traverse the Binary Tree.

## Approach
- Utilize DFS to traverse the tree.
- For each node, recursively traverse the left subtree, then recursively traverse the right subtree, and finally append the node value to the result list.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$