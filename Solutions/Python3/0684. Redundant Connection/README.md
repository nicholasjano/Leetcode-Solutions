# Solution Walk Through
Question: https://leetcode.com/problems/redundant-connection/

## Intuition
Since there are equal edges to nodes, I know that there must be a redundant connection. I can use the union find algorithm to check if any edge has both nodes with the same root, as that would be the redundant connection edge.

## Approach
- Loop through each edge and union them.
- If for any edge of two nodes the result is `node1_group == node2_group`, this means that with this edge, a cycle would be created, so it is a redundant connection.

## Time Complexity
$O(n + E \cdot α(n))$

$n$ represents the total number of nodes. \
$E$ represents the total number of edges.

## Space Complexity
$O(n)$