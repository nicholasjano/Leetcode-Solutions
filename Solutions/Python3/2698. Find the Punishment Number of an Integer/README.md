# Solution Walk Through
Question: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

## Intuition
I can loop through each fromber from `1` to `n`, and check if its square can be partitioned to make the initial value. To do the partitioning, I can use backtracking to check every possible case.

## Approach
- Create a loop that reaches every number from `1` to `n`.
- For each number, use a helper function to check if the square can be partitioned and summed into the original value
- In the helper function, backtracking is done to check every partition of the number using integer division and the modulus operator to split the number.

## Time Complexity
$O(n \cdot 2^{d})$

$d$ is the total number of digits in `n`.

## Space Complexity
$O(d)$