# Solution Walk Through
Question: https://leetcode.com/problems/delete-node-in-a-bst/

## Intuition
I can use a recursive solution to first find the key, then replace it's value with the value of the smallest value contained in the right subtree. This will make sure no other nodes need to move. In the case that the right or left subtrees do not exist past the key node, then just take whichever one does exists, if any, as the replacement node.

## Approach
- Base case `root` doesnt exist just return it.
- If the current `root` value is less than the key, move the root to the right and continue.
- If the current `root` value is greater than the key, move the root to the left and continue.
- If the key is never found, just return the root.
- If the key is found, see if it can be replaced by just the left or right subtree (if one or both don't exist).
- If both subtrees exist, replace the value of they key node with the smallest value from the right subtree, and delete the node that was the smallest value from the right subtree.

## Time Complexity
$O(h)$

$h$ is the height of the Binary Search Tree.

## Space Complexity
$O(h)$