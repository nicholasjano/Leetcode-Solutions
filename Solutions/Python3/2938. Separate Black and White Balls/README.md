# Solution Walk Through
Question: https://leetcode.com/problems/separate-black-and-white-balls/

## Intuition
I can use a two pointer approach for both ends of the string, and work towards the middle, the leftmost pointer looks for black balls, and the rightmost pointer looks for white balls. When I found the leftmost black ball and the rightmost white ball, I can swap them, keeping track of the swaps, and moving towards the middle.

## Approach
- Initiate two pointers, one at the leftmost index of the string, and what at the rightmost index of the string.
- Start by looking for the first black ball (if applicable) starting from the leftmost index of the string.
- Afterward, look for the first white ball (if applicable) starting from the rightmost index of the string.
- If both are found, swap those two balls, and save the amount of swaps required.
- Repeat this process until all the balls that need to be swapped have been swapped.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$