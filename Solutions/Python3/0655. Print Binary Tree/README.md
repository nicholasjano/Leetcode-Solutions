# Solution Walk Through
Question: https://leetcode.com/problems/print-binary-tree/

## Intuition
Find the max height of the tree, and create a 2d list with empty strings of the right proportion compared to the max height.
Place each node in their respective list index.

## Approach
- Account for the base case where the root is None, return an empty list.
- Use BFS to get the max height of the tree
- Create the 2d list template with emptry strings using the max height
- Use a double ended queue to store nodes to place on the 2d list.
Each item of the queue holds the node, the height of the node, and its index, all in a tuple
- Place the node into the 2d list. Create the offset for the child nodes. Append the child nodes into the queue.
- Loop through all nodes, leaving queue empty, then return the 2d list

## Time Complexity
$O(n)$

$n$ is the total number of nodes in the binary tree.

## Space Complexity
$O(h∗2^h)$

$h$ is the maximum height of the binary tree.