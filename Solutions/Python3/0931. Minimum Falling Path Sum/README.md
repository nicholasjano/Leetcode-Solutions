# Solution Walk Through
Question: https://leetcode.com/problems/minimum-falling-path-sum/

## Intuition
As with most dynamic programming questions, I begin with a recursive backtracking solution, and then add memoization. Afterward, I came up with a bottom up solution with extra memory. Finally, I realized that the extra memory array was the same format as `matrix`, so I decided to manipulate `matrix` inplace to have a bottomup solution with no extra memory.

## Approach
- Loop through the rows of the matrix backwards, skipping the final row as there will be no rows underneath to change the result.
- Loop through the columns for each row, and find the minimum falling path from that point, and update the column value to that value.
- Keep looping until the top row is complete, and then return the minimum falling path from the top row.

## Time Complexity
$O(n^2)$

## Space Complexity
$O(1)$