# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-level-order-traversal/

## Intuition
I can do a simple BFS on the binary tree, keeping track of the levels for the resulting table index.

## Approach
- Utilize a BFS for level-order traversal of the tree.
- Keep track of the level of each node, as it is used for the index within the final `result` list.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$