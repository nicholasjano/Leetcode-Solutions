# Solution Walk Through
Question: https://leetcode.com/problems/validate-binary-search-tree/

## Intuition
I can utilize BFS, while also maintaining the upper/lower bounds constraining each node.

## Approach
- Utilize a BFS for level-order traversal of the tree.
- Maintain the bounds a nodes value must meet. If the node is on the left of a parent/grandparent node, it must not have a value equal to or above that node. If the node is on the right of a parent/grandparent node, it must not have a value equal to or less that node.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$