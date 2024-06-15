# Solution Walk Through
Question: https://leetcode.com/problems/defanging-an-ip-address/

## Intuition
Create a new string, and iterate through the original string. I can append each chcaracter to the new string until I reach a '.' character, and in that case, I'll append '[.]' instead.

## Approach
- Initialize a new string to store the defanged IP
- Iterate through every character in address:
- If the character matches '.' I'll append '[.]' to the new string
- Otherwise, I'll append the original character to the new string

## Time Complexity
$O(n)$

## Space Complexity
$O(n)$