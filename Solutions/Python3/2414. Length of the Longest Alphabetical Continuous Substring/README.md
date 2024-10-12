# Solution Walk Through
Question: https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

## Intuition
Loop through the characters of `s`, comparing their respective ASCII values to determine if two adjacent characters are alphabetically continuous.

## Approach
- Loop through `s` starting at index 1, and comparing each character to the previous character to see if they are alphabetically continuous. If they are, extend the current streak, and save it as the longest if applicable.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$