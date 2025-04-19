# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Intuition
The key idea is that there will be one root node where that node takes the sums of both the left and right subtrees, while the rest only take the max in one direct path. To do this, for each node in the tree, calculate both the max if that node is the root, and the max if that node is not the root (in this case, just the max path in one direction is needed). Whichever node has the maximum sum as the root will have its sum returned as the final value.

## Approach
- Cover the base case if the root is none, return 0.
- Run a postorder traversal on the tree. For each node, calculate the maximum sum if that node was the root (right branch largest sum path plus left branch largest sum path, plus the nodes value). If this maximum sum is the new max, save it and pass it back up.
- Along with the maximum sum if that node was the root, also calculate the maximum sum if that node is not the root, by summing the nodes value with only the largest branch sum, not both.
- Pass both these values back up the traversal for higher level nodes to utilize, and at the end, return the maximum sum for the node that had the largest maximum sum as root.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$