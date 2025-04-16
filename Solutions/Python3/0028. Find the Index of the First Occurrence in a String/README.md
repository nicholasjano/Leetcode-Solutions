# Solution Walk Through
Question: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Intuition
For each index in `haystack`, check if starting at that index, `needle` can be formed.

## Approach
- Loop though the indicies of `haystack`, only for positions where `needle` can be formed.
- Nested loop through the indicies of `needle`, checking if each character matches with the character from `haystack`.
- If at any point a character does not match, break out of the loop and move to the next starting position in `haystack`.
- If all the characters in `needle` matched those of `haystack` from a certain point, return the starting position.
- If the outer loop exits with no return, return -1 as there is no match.

## Time Complexity
$O(n \cdot m)$

$n$ is the length of `haystack`. \
$m$ is the length of `needle`.

## Space Complexity
$O(1)$