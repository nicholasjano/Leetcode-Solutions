# Solution Walk Through
Question: https://leetcode.com/problems/reverse-integer/

## Intuition
Grab the last digit, add it to the result, and multiply the result by 10 for th next digit. For negative numbers, use `abs()` and return the sign at the end.

## Approach
- Keep a variable to hold whether `x` was originally negative. Convert `x` to its absolute value.
- For each digit in `x`, pull it, multiply the result by 10 (to get the proper digit placement), and add the digit to the result. Continue until each digit is accounted for.
- Check for edge cases if the integer surpasses the limit.
- If `x` was originally negative, flip the sign of the result and return it.

## Time Complexity
$O(\log_{10}(x))$

## Space Complexity
$O(1)$