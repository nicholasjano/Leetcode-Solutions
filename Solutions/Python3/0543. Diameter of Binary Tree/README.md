# Solution Walk Through
Question: https://leetcode.com/problems/diameter-of-binary-tree/

## Intuition
I can use a postorder trvaersal, counting the distance the left path and right paths take from each node, and update the diameter.

## Approach
- Run a DFS postorder traversal. Cover the base case if the node is None, return 0.
- For each node, get the length of its left and right paths, and update the diameter if there is a new max diameter found.
- Once each branch has been accounted, for return the diameter.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(h)$

$h$ represents the height of the tree.