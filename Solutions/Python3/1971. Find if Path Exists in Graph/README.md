# Solution Walk Through
Question: https://leetcode.com/problems/find-if-path-exists-in-graph/

## Intuition
This problem is a classic example of where the union-find algorithm would benefit. The union can set the parent of the node groups based off the edges, and the find can determine whether two noted have the same parent, meaning they are connected.

## Approach
- Setup the UnionFind class with methods for both union and find.
- For each edge, attempt to union the nodes.
- Check if the parent of the source and destination nodes are the same. If they are the same, there is a valid path from source to destination.

## Time Complexity
$O(n + E \cdot α(n))$

$E$ is the number of edges.

## Space Complexity
$O(n)$