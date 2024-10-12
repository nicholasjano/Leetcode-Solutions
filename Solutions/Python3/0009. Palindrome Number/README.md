# Solution Walk Through
Question: https://leetcode.com/problems/palindrome-number/

## Intuition
I can loop through `x` at most half the amount of digits. At each iteration, I can pull the last digit of `x` and place it in a new value, but in reverse order. I can then compare the two numbers and see if 

## Approach
- Cover the base case for negative numbers and numbers ending in 0.
- Loop through `x`, pulling out the ones digit with `x//10`, and placing it as the ones digit in the new number with `(reversed_half * 10) + (x % 10)`. This ensures that `reversed_half` holds a reversed iteration of the second half of `x`.
- Once `x` surpasses `reversed_half`, check if they equal (for even numbers) or if `x == (reversed_half // 10)` (for odd numbers).

## Time Complexity
$O(\log_{10}(n))$

$n$ represents the value of `x`.

## Space Complexity
$O(1)$