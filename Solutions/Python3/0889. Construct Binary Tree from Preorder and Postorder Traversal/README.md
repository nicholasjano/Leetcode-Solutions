# Solution Walk Through
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

## Intuition
Knowing the properties of preorder and postorder traversal, I know that the first element in preorder is always the root of the current subtree, and the last element in postorder is the root of the current subtree. The elements between help figure out where the left and right subtrees begin and end.

## Approach
- Create two pointers to track the preorder and postorder indicies.
- Start a recursive approach to build the tree
- Create a node using the current value from the preorder array.
- If the current nodes value isn't equal to the current value in the postorder array, recursively build the left subtree. After, if the nodes value still isn't equal to the current postorder value, recursively build the right subtree.
- Once the current node matches the current postorder value, that subtree is finished. Increment the postorder index and return the node.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(h)$

$h$ represents the height of the tree.