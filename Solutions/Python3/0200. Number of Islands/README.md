# Solution Walk Through
Question: https://leetcode.com/problems/number-of-islands/

## Intuition
I an go through each `(row, column)` pair in the grid until I reach a `"1"`. Once I do, I can use BFS to find the rest of the surrounding island, and mark it as `"0"` so I don't mark the same island twice. I constinue this until I've visted each `(row, column)` pair.

## Approach
- Loop through each row column pair until the resulting position is a `"1"`.
- Once the `"1"` is reached, run BFS, checking in each direction to find the whole island. Each visited `"1"` will be converted to a `"0"` to ensure the same island is not counted twice.
- Continue until the entire grid has been visited.

## Time Complexity
$O(n \cdot m)$

## Space Complexity
$O(n \cdot m)$