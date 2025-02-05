# Solution Walk Through
Question: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

## Intuition
I can loop through the strings, and when I find a character mismatch, I save it and check if a future mismatch is the opposite, meaning a swap could correct it.

## Approach
- Base case if the two strings are equal, the result will always be true
- Loop through each character of `s1` and `s2` and check if the characters match
- If a character swap was already previously found, return false as there is only up to 1 swap
- If this is the first mismatch, save the characters
- If the position of characters for a swap have been found previously, check to see if the current mismatch can make a swap with the previous position. If it can, then a proper swap has been found, if not, then return false as 2 swaps would be needed.

## Time Complexity
$O(n)$

$n$ is the length of `s1`.

## Space Complexity
$O(1)$