# Solution Walk Through
Question: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

## Intuition
I can loop through `words` from start to finish, and check if each word is a palindrome. If it is, return it. If none are found, I can just return the empty string.

## Approach
- Loop though each word in `words` from the start
- If the word is a palindrome return it
- If no palindromes are found, return the empty string

## Time Complexity
$O(n \cdot m)$

$n$ is the length of `words`. \
$m$ is the length of the longest word in `words`.

## Space Complexity
$O(1)$