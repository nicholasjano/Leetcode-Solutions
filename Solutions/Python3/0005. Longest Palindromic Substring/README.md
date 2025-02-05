# Solution Walk Through
Question: https://leetcode.com/problems/longest-palindromic-substring/

## Intuition
For odd lengthed palindromes, I can check each character in `s` as the center of the palindrome, and expand to get the largest string. For even lengthed palindromes, it's similar, but instead of checking each character, I check any adjacent duplicate characters.

## Approach
- Cover base cases for `s <= 2`
- Loop through each character in `s`, and expand it in each direction, and check if a palindrome can be created. Save the palindrome if it is the new largest.
- Loop through each character in `s`, check if the adjacent index is equal (for an even-lengthed palindrome), and expand the group in each direction, and check if a palindrome can be created. Save the palindrome if it is the new largest.

## Time Complexity
$O(n^2)$

$n$ is the length of `s`

## Space Complexity
$O(1)$