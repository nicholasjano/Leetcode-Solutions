# Solution Walk Through
Question: https://leetcode.com/problems/zero-array-transformation-ii/

## Intuition
I can use a difference array and a prefix sum of the accumulated reductions up to any point to greedily determine if I need to use more queries or not for the current number. If I do, I can grab the next query, and adjust the reductions based off the maximum increment. If I ever surpass all queries and there is still a number that has not reached 0, then I know that a zero-array is not possible.

## Approach
- Initialize a difference list to store new reductions starting at each position, as well as a prefix sum for total reductions.
- Loop through `nums`. First check if the current reductions can turn the current number to 0. If it can, then continue the loop.
- If the current number is above 0 even after reductions, grab the next queries until the current number can be reduced to 0. Ensure to not accumulate any reductions for past values as they are not needed anymore.
- If the current number can never reduce to 0, return -1, otherwise, continue until all numbers in `nums` have been accounted for, and return the position of the queries as the value of queries used.

## Time Complexity
$O(n + k)$

$n$ represents the length of `nums`. \
$k$ represents the length of `queries`.

## Space Complexity
$O(n)$