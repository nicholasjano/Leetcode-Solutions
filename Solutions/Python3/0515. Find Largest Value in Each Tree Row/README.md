# Solution Walk Through
Question: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

## Intuition
I can use BFS for a level-order traversal of the Binary tree. With this, for each node, I can use their level in the tree and compare their value to all other nodes with the same level, and only store the max.

## Approach
- Cover the base case if the root doesn't exist
- Place the root node and it's level in a queue, and conduct a level-order traversal using BFS
- For each node that is stored in the queue, also store the node's level along with it
- For each node, level pair, check if that node's value is the largest for that level. If it is, store it in `result` at the index of the level
- Once the level-order traversal is done, return `result`

## Time Complexity
$O(n)$

$n$ represents the total number of nodes in the tree.

## Space Complexity
$O(n)$