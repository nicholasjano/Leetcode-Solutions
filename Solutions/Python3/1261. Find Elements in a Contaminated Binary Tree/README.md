# Solution Walk Through
Question: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

## Intuition
I can traverse the tree using BFS and recover all the values according to the left/right rules. I can use a set to store all the recovered values and check if a target value exists.

## Approach
- Set up the set of seen recovered values and start the BFS from the root.
- For each node, add it to the set, preform calculations if necessary, and add the updated next node to the queue for BFS traversal.
- find:
    - Check if the `target` is within the set of recovered values.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$