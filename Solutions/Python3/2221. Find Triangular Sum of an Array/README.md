# Solution Walk Through
Question: https://leetcode.com/problems/find-triangular-sum-of-an-array/

## Intuition
I first came up with a solution where I calculated all the values manually. This was inefficient as it was $O(n^{2})$. So I came up with a math based approach where I can sum each value, multipled by how many occurences it will have in the final answer. The occurences are determined by the amount of paths a number can take from start to finish. This follows the pascals triangle pattern.

## Approach
- Cover the base case if `n == 1`, just return the value from the list.
- For each number in `nums`, add the value to the result multiplied by its occurences. The occurences are calculated by `times_element_appears = times_element_appears * positions_remaining // current_position`, starting and finishing at 1.
- Mod each result by 10.
- Once the one-pass loop is completed, return the result.

## Time Complexity
$O(n)$

## Space Complexity
$O(1)$