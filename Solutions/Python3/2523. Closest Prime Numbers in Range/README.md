# Solution Walk Through
Question: http://leetcode.com/problems/closest-prime-numbers-in-range/

## Intuition
I can iterate through the left/right range, identify prime numbers, and track pairs with the smallest gap.

## Approach
- Create a helper function to check if a given number is a prime number.
- Iterate through the range from left to right.
- For each prime number found, compare its distance to the previously found prime (if applicable). Store the pair with the minimum difference.
- If there is a pair with difference less than or equal to 2, return immediately as this must be optimal.
- Return the closest pair found, or `[-1, -1]` if no prime pair exists.

## Time Complexity
$O((right − left) \cdot \sqrt{right​})$

## Space Complexity
$O(1)$