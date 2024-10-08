# Solution Walk Through
Question: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

## Intuition
First I came up with a solution using a stack. This was good, but it used $O(n)$ space, so I knew I could do better. I can utilize a two-pointer approach to count the brackets on each end and find which two brackets would need a swap.

## Approach
- Start by moving from the start of the string to the end. Keep balance of every bracket that's ran into. An "[" is good (+1) as the start of the string needs more open brackets, and an "]" is -1. If the balance ever goes negative, a swap is needed.
- To swap, start navigating from the opposite side to find an "[" for the swap. Once found, complete the swap, update the banace, and continue from where the left-to-right traversal was last left off.
- Continue until the left pointer passes the right pointer, and return the swaps.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$