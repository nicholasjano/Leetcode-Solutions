# Solution Walk Through
Question: https://leetcode.com/problems/most-profitable-path-in-a-tree/

## Intuition
I can use DFS to find the maximum profit by checking for who reaches each node first. Alice from the root, or Bob from his starting position.

## Approach
- Create an adjacency list representation of the tree from the edges.
- Use DFS to calculates both the distances from Bob to each node, and the maximum income Alice can earn along each path.
- For each node, check who reaches it first. If Alice reaches it before Bob, she gets the full amount. If Bob reaches first, Alice gets nothing. If they reach at the same time, Alice gets half.
- Get the maximum possible income by choosing the most profitable path from the root to any leaf.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$