# Solution Walk Through
Question: https://leetcode.com/problems/powx-n/

## Intuition
Account for base cases, flip values for a negative power, multiply the value by itself, and integer divide the power by 2 until it is 0.

## Approach
- Account for the base case of n = 0 return 1, as any number to the power of 0 is equal to 1
- If the exponent n is negative, turn x into its reciprocal and change the sign of n to positive
- Initialize the result and current variables
- Check if n is odd, and multiply the result by the current product if it is odd
- Multiply the current product by itself
- Preform integer divison on n to half floor it, and loop until n is 0

## Time Complexity
$O(logn)$

## Space Complexity
$O(1)$