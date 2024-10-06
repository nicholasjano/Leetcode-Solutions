# Solution Walk Through
Question: https://leetcode.com/problems/score-of-a-string/

## Intuition
Loop through the string and for each adjacent pair of letters, get their ASCII values using `ord()`, find the difference, and use `abs()` to get the absolute value of the difference. Sum these values throughout the whole string, and you have the score.

## Approach
- Loop through `s`. For each index, take the adjacent pair of `s[i]` and `s[i+1]`, get the difference between their ASCII values, get the absolute value, and add it to the score.
- Once `s` has been complete, return the score.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(1)$