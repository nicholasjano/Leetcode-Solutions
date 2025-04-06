# Solution Walk Through
Question: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

## Intuition
I can utilize a level-order traversal, but include an extra queue per level, what will be reversed ever other level.

## Approach
- Preform a regular level-order traversal with BFS.
- In addition, for each level, use another queue called `curr_level_queue`. If `level % 2 == 0` with levels starting as 0, the `curr_level_queue` will be the same order as the regualr queue was for the level. Otherwise, it will be reversed.
- At the end of each level traversal, add `curr_level_queue` to the final traversal list for that levels nodes instead of just adding the nodes individually, and continue to the next level if applicable.

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$