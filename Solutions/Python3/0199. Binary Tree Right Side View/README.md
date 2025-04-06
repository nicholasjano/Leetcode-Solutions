# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-right-side-view/

## Intuition
I can utilize a variation of preorder traversal, navigating the right side first, and storing the rightmost nodes at each level.

## Approach
- Preform a DFS preorder traversal, going right before left, and keeping track of the level of each node.
- If the level has not been visited yet, append the node to the traversal result list.
- Once each node has been visited, return the traversal result list.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(h)$

$n$ represents the height of the tree.