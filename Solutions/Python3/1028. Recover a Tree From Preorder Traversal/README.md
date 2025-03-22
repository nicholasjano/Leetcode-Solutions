# Solution Walk Through
Question: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

## Intuition
I can parse the traversal string to get the depth and value of each node, and then use recursion to rebuild the tree.

## Approach
- Parse the traversal string to extract each nodes depth and value and store them in a double ended queue.
- Call a recurive function to build the tree.
- Cover the base case if there are no more nodes left or if the depth doesn't match.
- Pop the front node information from the deque and create a node with the current value, and build the left/right subtrees for that node.
- Continue until every node is accounted for.


## Time Complexity
$O(n)$

$n$ represents the length of the string `traversal`.

## Space Complexity
$O(n)$