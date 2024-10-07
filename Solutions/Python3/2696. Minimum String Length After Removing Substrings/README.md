# Solution Walk Through
Question: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

## Intuition
I first considered using a two-pointer approach, but this would lead to repeating some values within the string. I ended up using a stack to track the charatcers in order of most recently visited, and I can easily compare and pop for the substrings.

## Approach
- For each character in the `s`, I compare it with the most recent value added to the stack to see if a substring can be formed.
- If a substring can be formed, pop the value from the stack, and discard that character as well as the current character. The logic to check whether a substring can be formed utilized the ASCII values from the characters.
- If a substring cannot be formed, append the current character into the stack.
- The resulting length of the stack will be the minimum possible length of the resulting string.

## Time Complexity
$O(n)$

$n$ is the length of `s`.

## Space Complexity
$O(n)$