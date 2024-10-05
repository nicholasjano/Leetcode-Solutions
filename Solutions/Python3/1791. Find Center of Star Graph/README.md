# Solution Walk Through
Question: https://leetcode.com/problems/find-center-of-star-graph/

## Intuition
Since each node only connects to the center node, I can just find the common node between two connections, and that node will be the center node. No matter the size of the graph, I only need two connections to find the center.

## Approach
- Store the first connection in the variable `first`.
- Loop through the two nodes in the second connection, and whichever node is also in `first` is returned.

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$