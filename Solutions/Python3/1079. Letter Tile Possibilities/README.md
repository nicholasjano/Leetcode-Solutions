# Solution Walk Through
Question: https://leetcode.com/problems/letter-tile-possibilities/

## Intuition
I can put the remaining letters from `tiles` in a counter dictionary, and I can recursively go through each of the remaining letters to create a new sequence, count it, backtrack, and repeat until every combination has been reached.

## Approach
- Get the count of each letter in `tiles` using a counter dictionary
- Call a recursive function with the current state of the counter dictionary
- Loop through each character (A-Z) and check if it has any remaining occurrences to use
- Remove the occurrence of a character that still needs to be used, increment the total sequence by 1, and continue with the updated counter dictionary
- When backtracked, add the occurrence of the character back so every sequence can be reached

## Time Complexity
$O(n!)$

$n$ is the length of `tiles`.

## Space Complexity
$O(n)$