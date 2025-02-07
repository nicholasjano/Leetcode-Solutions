# Solution Walk Through
Question: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

## Intuition
I can start at the bottom left, navigate up the column until a negative number is found, then move to the next in the row and continue.

## Approach
- Set up variables to start at the bottom left index of the grid
- Create a while loop with the exiting condition being that the current position is out of the grid bounds
- In the loop, move up the column until a negative number is found, then move to the next in the row and continue
- Once a negative is found, add `(n - col)` to the negative counter before moving on as the rest will be negative since the grid is in non-increasing order

## Time Complexity
$O(m + n)$

## Space Complexity
$O(1)$