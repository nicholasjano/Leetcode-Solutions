# Solution Walk Through
Question: https://leetcode.com/problems/smallest-even-multiple/

## Intuition
When n is even, it is already a multiple of 2. When n is odd, the smallest even multiple will just be n * 2.

## Approach
- Check if n is even:
- If n is even, return n
- If n is odd, return 2*n

## Time Complexity
$O(1)$

## Space Complexity
$O(1)$