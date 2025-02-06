# Solution Walk Through
Question: https://leetcode.com/problems/univalued-binary-tree/

## Intuition
I can utilize BFS to navigate the tree, and make sure every node matches the root's value.

## Approach
- Save the value of the root node as the uni-value
- Utilize a BFS for level-order traversal of the tree
- For each node, check if the value matches the value of the root
- If the values do not match, this is not a uni-valued tree, so return False
- If the entire tree has been navigated and no derivation in values were found, return True

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$