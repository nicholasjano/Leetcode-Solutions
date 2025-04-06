# Solution Walk Through
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Intuition
I can use a variation of post-order traversal where I search until I found either `p` or `q`. If a parent node finds both `p` and `q` to the right and left of it, then that node will be the lowest common ancestor. If a parent node only finds one, that node will be the lowest common ancestor, as it will be somewhere under that one that was found.

## Approach
- Cover the base case of if the node doesn't exist, or if it is `p` or `q`. Return the node in this case.
- Recursively reach the left and right branches for `p` or `q`.
- If at any node, both left branch and right branch find one of the values, that node will be returned as the lowest common ancestor.
- If only one of `p` or `q` can be found (only left or right is true), then the node that was found (`p` or `q`) will be the lowest common ancestor.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(h)$

$h$ represents the height of the tree.